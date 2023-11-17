import datetime
from rest_framework import serializers
from AppUser.models import AppUser
from AppUser.models import VerifyCode


class LoginAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            "username",
            "password",
        ]

    def validate_username(self, username):
        # 检查长度
        if len(username) < 4 or len(username) > 20:
            raise serializers.ValidationError(
                "Username Length Error")
        # 检查是否由字母与数字组成
        if not username.isalnum():
            raise serializers.ValidationError("Username Format Error")
        return username

    def validate_password(self, password):
        # 检查长度
        if len(password) < 4 or len(password) > 20:
            raise serializers.ValidationError(
                "Password length Error")
        # 检查是否由字母与数字组成，且必须含有字母
        if not password.isalnum() or password.isdigit():
            raise serializers.ValidationError(
                "Password Format Error")
        return password


class RegisterAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = [
            "username",
            "password",
            "email",
        ]

    def validate_username(self, username):
        # 检查长度
        # password = super.validate_password(password)
        if len(username) < 4 or len(username) > 20:
            raise serializers.ValidationError(
                "Username Length Error",
            )
        # 检查是否由字母与数字组成
        if not username.isalnum():
            raise serializers.ValidationError("Username Format Error")
        # 检查是否有重复用户名
        # if AppUser.objects.filter(username=username).exists():
        #     raise serializers.ValidationError("Username already exists")
        return username

    def validate_password(self, password):
        # 检查长度
        # password = super.validate_password(password)
        if len(password) < 4 or len(password) > 20:
            raise serializers.ValidationError(
                "Password length Error")
        # 检查是否由字母与数字组成，且必须含有字母
        if not password.isalnum() or password.isdigit():
            raise serializers.ValidationError(
                "Password Format Error")
        return password

    # def validate_email(self, email):
    #     # 检查是否有重复邮箱
    #     if AppUser.objects.filter(email=email).exists():
    #         raise serializers.ValidationError("Email already exists")
    #     return email

class VerifyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifyCode
        fields = [
            "code",
            "email",
        ]

    def validate_code(self, code):
        if len(code) != 6:
            raise serializers.ValidationError("Code length error")
        return code

    # def validate_email(self, email):
        # 检查一分钟内是否已经向该邮箱发送过验证码
    #     # 检查邮箱格式
    #     if not email.endswith("@pku.edu.cn") :
    #         raise serializers.ValidationError("Email Format Error")
    #     # 检查是否有重复邮箱
    #     if VerifyCode.objects.filter(email=email).exists():
    #         raise serializers.ValidationError("Email already exists")
    #     return email