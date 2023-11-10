from django.http import HttpResponse
from django.shortcuts import render
from .models import User

#todo 与数据库交互
#todo 与前端交互: 加密信息
#todo 优化登录与注册的逻辑

def toLoginView(request):
    return render(request, 'login.html')


def loginView(request):
    username = request.POST.get('user', '')  # 后面的''表示获取不到user就赋值空
    password = request.POST.get('pwd', '')
    if username and password:
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("请输入正确用户名和密码！")

def toRegisterView(request):
    return render(request, 'register.html')

def registerView(request):
    username = request.POST.get('user', '')  # 后面的''表示获取不到user就赋值空
    password = request.POST.get('pwd', '')
    if username and password:
        return HttpResponse("注册成功！")
    else:
        return HttpResponse("请输入正确用户名和密码！")