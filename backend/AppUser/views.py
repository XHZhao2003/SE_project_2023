from django.utils import timezone
from django.http import JsonResponse
from AppUser.models import AppUser, VerifyCode
from AppUser.serializer import LoginAppUserSerializer, RegisterAppUserSerializer, VerifyCodeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from AppUser.verify import generate_code
from AppUser.rsa_crypt import *


class AppUserView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        action = request.data.get("action")
        if action == 'register':
            return self.register(request)
        elif action == 'login':
            return self.login(request)
        elif action == 'send_email':
            return self.send_email(request)
        else:
            return Response({'error': 'Invalid action {},{}'.format(request.data, action)}, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def send_email(self, request):
        email = request.data.get('email')
        create_time = timezone.now()

        verifiycode = VerifyCode.objects.filter(email=email)
        # 若有十分钟前发送的验证码，则在数据库中删除对应的对象
        # 禁止一分钟内重复发送验证码
        for code in verifiycode:
            if (create_time - code.create_time).seconds < 60:
                return Response(data={
                    "msg": "please wait for 60 seconds",
                    "status": status.HTTP_400_BAD_REQUEST
                })
            if (create_time - code.create_time).seconds > 600:
                code.delete()

        # 生成随机验证码
        code = generate_code()
        while(VerifyCode.objects.filter(code=code).exists()):
            code = generate_code()
        
        # 将验证码存入数据库
        code_data = {'email': email,
                'code': code}
        serilizer = VerifyCodeSerializer(data=code_data)

        try:
            serilizer.is_valid(raise_exception=True)
            serilizer.save()
        except Exception as e:
            # 打印出serilizer中储存的数据
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })
        
        # 发送邮件
        message = "\n".join([u'您的验证码是：', code, u'该验证码有效期为10分钟', u'请勿回复该邮件，谢谢！', u'ERoad app team'])
        try:
            succ_num = send_mail(u'ERoad app team', message,
                                 settings.EMAIL_HOST_USER, [email])
            if succ_num == 1:
                return Response(data={
                    "msg": "send email successfully",
                    "status": status.HTTP_200_OK
                })
            else:
                return Response(data={
                    "msg": "send email failed",
                    "status": status.HTTP_400_BAD_REQUEST
                })
        except Exception as e:
            return Response(data={
                "msg": "send email failed,"+str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password = decrypt_data(password)
        email = request.data.get('email')
        confirm = request.data.get('confirm')
        verify_code = request.data.get('verify_code')
        if confirm != password:
            return Response(data={
                "msg": "Password not match",
                "status": status.HTTP_400_BAD_REQUEST
            })

        # 验证验证码是否正确
        verified = False
        time_now = timezone.now()
        verifiycode = VerifyCode.objects.filter(email=email)
        for code in verifiycode:
            if code.code == verify_code and (time_now - code.create_time).seconds < 600:
                verified = True
                break
            if (time_now - code.create_time).seconds > 600:
                code.delete()
        if not verified:
            return Response(data={
                "msg": "Invalid verify code",
                "status": status.HTTP_400_BAD_REQUEST
            })

        data = {'username': username, 'email': email,
                'password': password}

        serilizer = RegisterAppUserSerializer(data=data)
        try:
            serilizer.is_valid(raise_exception=True)
            serilizer.save()

            return Response(data={
                "msg": "register successfully",
                "status": status.HTTP_201_CREATED
            })
        except Exception as e:
            return Response(data={
                "msg": str(e),
                "status": status.HTTP_400_BAD_REQUEST
            })

    @csrf_exempt
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        password = decrypt_data(password)
        # 如果username中含有@，则按照email进行登录
        if '@' in username:
            users = AppUser.objects.filter(email=username)
        else:
            users = AppUser.objects.filter(username=username)

        if not users.exists():
            return Response(data={
                "msg": "username or email does not exist",
                "status": status.HTTP_400_BAD_REQUEST
            })

        user = users.first()
        if user.password != password:
            return Response(data={
                "msg": "password is wrong",
                "status": status.HTTP_400_BAD_REQUEST
            })

        # token = user.generate_token()
        serializer = LoginAppUserSerializer(user)
        return Response(data={
            "msg": "login successfully",
            # "token": token,
            # "user": serializer.data,
            "status": status.HTTP_200_OK
        })

