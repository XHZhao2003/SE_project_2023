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
        if(action == 'get_all'):
            return self.get_all(request)

    @csrf_exempt
    def get_all(self, request):
        all_roads = Road.objects.all()
        # for road in all_roads:
        #     print(road.name)
        serializer = RoadSerializer(all_roads, many=True)
        return Response(serializer.data)
        