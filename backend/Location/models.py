from django.db import models


class Location(models.Model):
    number = models.IntegerField(default=-1)
    name = models.CharField(max_length=100, unique=True, default="")
    opening_hours = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    x = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    y = models.DecimalField(decimal_places=10, max_digits=15, default=0)

class Comment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)
    username = models.CharField(max_length=10000)
    timestamp = models.DateTimeField()
    
class TagFunction(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

class TagPlace(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    
class TagTime(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)

