from Road.models import Road, Point
from Road.serializer import RoadSerializer, PointSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from django.shortcuts import render


class RoadError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class RoadView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if action == 'get_all':
            return self.get_all(request)
        elif(action == 'get_road_crowding'):
            return self.get_road_crowding(request)
        elif(action == 'feedback_road_crowding'):
            return self.feedback_road_crowding(request)
        else:
            return Response(data={
                "msg": str(RoadError("action error")),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def get_all(self, request):
        '''
        返回所有路径的信息
        '''
        try:
            name = []
            number = []
            points = []
            feedback = []
            all_roads = Road.objects.all()
            for road in all_roads:
                name.append(road.name)
                number.append(road.number)
                feedback.append(road.feedback)

                Points = Point.objects.filter(road=road)
                if len(Points) != road.num_of_points:
                    raise RoadError("num_of_points of road " + str(road.number) +
                                    " is not equal to the number of points in database")

                points.append([(point.x, point.y) for point in Points])

            return Response(data={
                "name": name,
                "id": number,
                "points": points,
                "feedback": feedback,
                "status": status.HTTP_200_OK
            })
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def get_road_crowding(self, request):
        '''
        根据前端传来的路的名字（序号），返回该路的所有信息
        '''
        try:
            number = request.data.get("id")
            road = Road.objects.get(number=number)
            feedback = road.feedback
            #print('crowd: ', road.crowd, 'feedback: ', feedback)
            feedback_std = self.crowd2feedback((int)(road.crowd))

            if feedback != feedback_std:
                road.feedback = feedback_std
                road.save()
                feedback = road.feedback

            return Response(data={
                "id": number,
                "feedback": feedback,
                "status": status.HTTP_200_OK
            })

        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    def crowd2feedback(self, crowd):
        '''
        根据路的拥挤程度，返回路的反馈信息
        '''
        if crowd <= 30:
            return 1
        elif crowd <= 100:
            return 2
        elif crowd <= 150:
            return 3
        else:
            return 4

    @csrf_exempt
    def feedback_road_crowding(self, request):
        '''
        根据前端传来的路的名字（序号）和点的序号，返回该点的反馈信息
        '''
        try:
            number = request.data.get("id")
            info = request.data.get("road_crowding")
            road = Road.objects.get(number=number)
            if road is None:
                raise RoadError("road " + str(number) + " does not exist")

            road.crowd += (int)(info)
            if road.crowd < -30:
                road.crowd = -30
            elif road.crowd > 250:
                road.crowd = 250

            road.feedback = self.crowd2feedback(road.crowd)
            road.save()

            return Response(data={
                "msg": "feedback success",
                "status": status.HTTP_200_OK
            })

        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })


# todo : 这里的api调用暂时未被启用，后续根据实际情况考虑，可以结合用户权限维护管理员功能
class AdminView(APIView):
    '''
    管理员创建路的信息
    '''

    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if(action == 'create_road'):
            return self.create_road(request)
        elif(action == 'create_point'):
            return self.create_point(request)
        else:
            return Response(data={
                "error": str(RoadError("action error")),
                "status": status.HTTP_400_BAD_REQUEST
            })

    def create_road(self, request):
        '''
        创建一条路
        '''
        try:
            number = request.data.get("number")
            # 若该路已存在，则返回错误信息
            # if(Road.objects.filter(number=number)):
            #     raise RoadError("road already exists")

            num_of_points = request.data.get("num_of_points")
            # if(num_of_points > 4):
            #     raise RoadError("num_of_points error")

            base_color = request.data.get("base_color")
            hover_color = request.data.get("hover_color")
            road = RoadSerializer(data={
                "number": number,
                "num_of_points": num_of_points,
                "base_color": base_color,
                "hover_color": hover_color
            })

            if(not road.is_valid()):
                raise RoadError("RoadSerializer error")
            road.save()

            return Response(data={
                "status": status.HTTP_200_OK
            })

        except Exception as e:
            return Response(data={
                "error": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    def create_point(self, request):
        '''
        创建一条路的一个点
        '''
        try:
            number = request.data.get("number")
            # 若该路不存在，则返回错误信息
            if(not Road.objects.filter(number=number)):
                raise RoadError("road not exists")

            x = request.data.get("point_loc")[0]
            y = request.data.get("point_loc")[1]
            if(x < 0 or y < 0):
                raise RoadError("point_loc error")

            road = Road.objects.get(number=number)
            point = PointSerializer(data={
                "road": road,
                "x": x,
                "y": y,
                "crowd": 0,
                "feedback": "smooth"
            })
            if(not point.is_valid()):
                raise RoadError("PointSerializer error")
            point.save()

            return Response(data={
                "status": status.HTTP_200_OK
            })

        except Exception as e:
            return Response(data={
                "error": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })
