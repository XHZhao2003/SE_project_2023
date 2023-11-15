from django.db import models

class AppUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_activity = models.BooleanField(default=False) # 是否通过邮箱验证码激活
    
    def __str__(self):
        return self.username

class VerifyCode(models.Model):
    code = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email