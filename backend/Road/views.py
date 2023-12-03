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
        if(action == 'get_all'):
            return self.get_all(request)
        elif(action == 'get'):
            return self.get(request)
        elif(action == 'feedback_crowding'):
            return self.feedback(request)
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
            number = []
            points = []
            base_color = []
            hover_color = []
            feedback = []
            all_roads = Road.objects.all()
            for road in all_roads:
                number.append(road.number)
                base_color.append(road.base_color)
                hover_color.append(road.hover_color)
                feedback.append(road.feedback)

                Points = Point.objects.filter(road=road)
                if len(Points) != road.num_of_points:
                    raise RoadError("num_of_points of road " + str(road.number) + " is not equal to the number of points in database")
                points.append([(point.x, point.y) for point in Points])

            return Response(data={
                "id": number,
                "base_color": base_color,
                "hover_color": hover_color,
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
    def get(self, request):
        '''
        根据前端传来的路的名字（序号），返回该路的所有信息
        '''
        try:
            number = request.data.get("id")
            road = Road.objects.get(number=number)
            feedback = road.feedback
            return Response(data={
                "name": number,
                "base_color": road.base_color,
                "hover_color": road.hover_color,
                "points_loc": points_loc,
                "feedback": feedback,
                "status": status.HTTP_200_OK
            })
        
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    def get_feedback(crowd):
        if crowd <= 30:
            return "smooth"
        elif crowd <= 100:
            return "crowded"
        else:
            return "blocked"

    @csrf_exempt
    def feedback(self, request):
        '''
        根据前端传来的路的名字（序号）和点的序号，返回该点的反馈信息
        '''
        try:
            number = request.data.get("number")
            point_x = request.data.get("point_x")
            point_y = request.data.get("point_y")
            info = request.data.get("info")
            road = Road.objects.get(number=number)
            if road is None:
                raise RoadError("road " + str(number) + " does not exist")
            
            point = Point.objects.get(road=road, x=point_x, y=point_y)
            if point is None:
                raise RoadError("point " + str(point_x) + " " + str(point_y) + " does not exist")

            if point.crowd < 10000 and info == 'crowded':
                point.crowd += 1
            elif point.crowd > 0 and info == 'smooth' :
                point.crowd -= 1

            point.feedback = self.get_feedback((int)(point.crowd))

            point.save(update_fields=['crowd', 'feedback'])
            return Response(data={
                "msg": "feedback success",
                "status": status.HTTP_200_OK
            })

        except Exception as e:
            return Response(data={
                "msg": str(e),
                "extra": str(point.crowd)+str(type(point.crowd)),
                "status": status.HTTP_400_BAD_REQUEST
            })


# todo : 这里的api调用暂时不被启用，后续根据实际情况考虑，可以结合用户权限维护管理员功能
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
            #若该路已存在，则返回错误信息
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
            #若该路不存在，则返回错误信息
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
