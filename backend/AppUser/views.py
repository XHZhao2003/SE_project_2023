from django.http import JsonResponse
from AppUser.models import AppUser
from AppUser.serializer import AppUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt



@api_view(['GET',])
@csrf_exempt
def appuser_list(request):
    if request.method == 'GET':
        appusers = AppUser.objects.all()
        serializer = AppUserSerializer(appusers, many=True)
        return Response(serializer.data)
    
    
@api_view(['POST',])
@csrf_exempt
def RegisterAppUser(request):
    serializer = AppUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
@csrf_exempt
def LoginAppUser(request):
    pass