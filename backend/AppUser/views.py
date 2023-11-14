from django.http import JsonResponse
from AppUser.models import AppUser
from AppUser.serializer import LoginAppUserSerializer, RegisterAppUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt



class AppUserView(APIView):
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        action = request.data.get("action")
        if action == 'register':
            return self.register(request)
        elif action == 'login':
            return self.login(request)
        else:
            return Response({'error': 'Invalid action {},{}'.format(request.data,action)}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def register(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        confirm = request.data.get('confirm')
        if confirm != password:
            return Response(data = {
                "msg": "Password not match",
                "status": status.HTTP_400_BAD_REQUEST
            })

        data = {'username': username, 'email': email, 'password': password}

        serilizer = RegisterAppUserSerializer(data=data)
        try:
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
            return Response(data = {
                "msg": "Register successfully",
                "status": status.HTTP_201_CREATED
            })
        except Exception as e:
            return Response(data = {
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def login(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        # 如果username中含有@，则按照email进行登录
        if '@' in username:
            users = AppUser.objects.filter(email=username)
        else:
            users = AppUser.objects.filter(username=username)
        
        if not users.exists():
            return Response(data = {
                "msg": "username or email does not exist",
                "status": status.HTTP_400_BAD_REQUEST
            })
        
        user = users.first()
        if user.password != password:
            return Response(data = {
                "msg": "password is wrong",
                "status": status.HTTP_400_BAD_REQUEST
            })

        # token = user.generate_token()
        serializer = LoginAppUserSerializer(user)
        return Response(data = {
            "msg": "login successfully",
            # "token": token,
            # "user": serializer.data,
            "status": status.HTTP_200_OK
        })

