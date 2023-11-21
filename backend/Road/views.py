from Road.models import Road
from Road.serializer import RoadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from django.shortcuts import render

class RoadView(APIView):
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if action == 'get_all':
            return self.get_all(request)
        if action == 'get_road_crowding':
            return self.get_road_crowding(request)

    @csrf_exempt
    def get_all(self, request):
        all_roads = Road.objects.all()
        # for road in all_roads:
        #     print(road.name)
        serializer = RoadSerializer(all_roads, many=True)
        return Response(serializer.data)
        
    @csrf_exempt
    def get_road_crowding(self, request):
        rd_id = request.data.get('id')
        road = Road.objects.filter(id=rd_id).first()
        crowding = self.Feedback2Crowding(road.feedback_1, road.feedback_2, 
                                          road.feedback_3, road.feedback_4)
        color = self.Crowding2Color(crowding)
        return Response(data={
            "id" : rd_id,
            "crowding" : crowding,
            "color": color
        })
    
    def Feedback2Crowding(self, fb1, fb2, fb3, fb4):
        # 这里需要换个算法
        if fb4 > 0:
            return 80
        elif fb3 > 0:
            return 60
        elif fb2 > 0:
            return 40
        else:
            return 20
    
    def Crowding2Color(self, crowding):
        # 这里需要换个算法
        if crowding == 80:
            return "#ff3333"
        elif crowding == 60:
            return "#df7401"
        elif crowding == 40:
            return "#dfe534"
        else:
            return "#46bc1d"