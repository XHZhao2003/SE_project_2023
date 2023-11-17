from django.contrib import admin
from .models import AppUser, VerifyCode

# Register your models here.
admin.site.register(AppUser)
admin.site.register(VerifyCode)
