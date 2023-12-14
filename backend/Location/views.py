from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Location, Comment, TagFunction, TagPlace, TagTime, Location_Function, Location_Place, Location_Time
from .serializer import CommentSerialzier
from rest_framework import status
import datetime


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
        elif action == "get_all_locations":
            return self.get_all_locations(request)
        elif action == 'post_comment':
            return self.post_comment(request)
        elif action == 'search_location':
            return self.search_location(request)
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
            location = self.GetLocationDictById(id)
            return Response(data=location)
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })
            
    @csrf_exempt
    def get_all_locations(self, request):
        '''
        返回所有地点的信息
        '''
        try:
            locations = Location.objects.all()
            locations_ = []
            for location in locations:
                location_dict = {
                    "id": location.number,
                    "name": location.name,
                    "x": location.x,
                    "y": location.y,
                }
                locations_.append(location_dict)
                
            return Response(data={
                "locations": locations_
            })
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })
    
    @csrf_exempt
    def post_comment(self, request):
        content, username, id, location = "", "", "", ""
        try:
            content = request.data.get("content")
            username = request.data.get("username")
            id = request.data.get("id")
            location = Location.objects.get(number=id)
            data = {
                "location": location.id,
                "content": content,
                "username": username,
                "timestamp": datetime.datetime.now()
            }
            serializer = CommentSerialzier(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })
        return Response(data={"id": id})

    @csrf_exempt
    def search_location(self, request):
        try:
            locations = Location.objects.all()
            filteredlocations = []
            tags = request.data.get('tags')
            tags1, tags2, tags3 = tags[0], tags[1], tags[2]
            for location in locations:
                containTag1 = False
                containTag2 = False
                containTag3 = False   
                # 功能 tag
                filteredTags1 = Location_Function.objects.filter(location=location)
                filteredTags1 = [locationTag.tag.id for locationTag in filteredTags1]
                for tag1 in tags1:
                    if tag1 in filteredTags1:
                        containTag1 = True
                        break
                # 地点tag
                if 8 in tags or tags2 == []:   # ALL or No tag2
                    containTag2 = True
                else:
                    filteredTags2 = Location_Place.objects.filter(location=location)
                    filteredTags2 = [locationTag.tag.id for locationTag in filteredTags2]
                    for tag2 in tags2:
                        if tag2 in filteredTags2:
                            containTag2 = True
                            break
                # 时间 tag
                if 25 in tags3 or tags3 == []:   # ALL or No tag3
                    containTag3 = True
                else:
                    filteredTags3 = Location_Place.objects.filter(location=location)
                    filteredTags3 = [locationTag.tag.id for locationTag in filteredTags3]
                    for tag3 in tags3:
                        if tag3 in filteredTags3:
                            containTag3 = True
                            break
                if containTag1 and containTag2 and containTag3:
                    filteredlocations.append(location)
            filteredlocationsDict = []
            for location in filteredlocations:
                dict = self.GetLocationDictById(location.id)
                filteredlocationsDict.append(dict)
            return Response(data={
                "result": filteredlocationsDict,
            })
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    def GetLocationDictById(self, id):
        location = Location.objects.get(number=id)
        comments = Comment.objects.filter(location=location)
        tags1 = Location_Function.objects.filter(location=location)
        tags2 = Location_Place.objects.filter(location=location)
        tags3 = Location_Time.objects.filter(location=location)
        commentsDict = []
        tags1List = []
        tags2List = []
        tags3List = []
        for comment in comments:
            dic = {
                "content": comment.content,
                "username": comment.username,
                "timestamp": comment.timestamp
            }
            commentsDict.append(dic)
        for tag1 in tags1:
            tags1List.append(tag1.tag.number)
        for tag2 in tags2:
            tags2List.append(tag2.tag.number)
        for tag3 in tags3:
            tags3List.append(tag3.tag.number)    
        return {
                "id": location.number,
                "name": location.name,
                "x": location.x,
                "y": location.y,
                "opening_hours": location.opening_hours,
                "description": location.description,
                "comments": commentsDict,
                "tags": [tags1List, tags2List, tags3List],
            }

            
                
            
