from django.contrib import admin
from .models import Location, Comment, TagFunction, TagPlace, TagTime, Location_Function, Location_Place, Location_Time

# Register your models here.
admin.site.register(Location)
admin.site.register(Comment)
admin.site.register(TagFunction)
admin.site.register(TagPlace)
admin.site.register(TagTime)
admin.site.register(Location_Function)
admin.site.register(Location_Place)
admin.site.register(Location_Time)