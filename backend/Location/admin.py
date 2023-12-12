from django.contrib import admin
from .models import Location, Comment, TagFunction, TagPlace, TagTime

# Register your models here.
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(TagFunction)
admin.site.register(TagPlace)
admin.site.register(TagTime)