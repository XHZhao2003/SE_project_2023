from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from models import Location, Comment, TagFunction, TagPlace, TagTime
from rest_framework import status


from django.shortcuts import render

class LocationError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class LocationView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if action == 'get_location_by_id':
            return self.get_location_by_id(request)
        else:
            return Response(data={
                "msg": str(LocationError("action error")),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def get_location_by_id(self, request):
        '''
        返回指定地点的信息
        '''
        try:
            id = request.data.get('id')
            location = Location.objects.get(number=id)
            comments = Comment.objects.filter(location=location)
            tags1 = TagFunction.objects.filter(location=location)
            tags2 = TagPlace.objects.filter(location=location)
            tags3 = TagTime.objects.filter(location=location)
            comments_ = []
            tags1_ = []
            tags2_ = []
            tags3_ = []
            for comment in comments:
                dic = {
                    "content": comment.content,
                    "username": comment.username,
                    "timestamp": comment.timestamp
                }
                comments_.append(dic)
            for tag1 in tags1:
                tags1_.append(tag1.number)
            for tag2 in tags2:
                tags2_.append(tag2.number)
            for tag3 in tags3:
                tags3_.append(tag3.number)
                
            return Response(data={
                "name": location.name,
                "opening_hours": location.opening_hours,
                "description": location.description,
                "comments": comments,
                "tags": [tags1_, tags2_, tags3_],
                "status": status.HTTP_200_OK
            })
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })