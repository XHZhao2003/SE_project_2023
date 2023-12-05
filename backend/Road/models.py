from django.db import models


class Road(models.Model):
    number = models.IntegerField(default=-1)
    # 前端定义折线的节点数量，规定最大不超过4
    num_of_points = models.IntegerField()
    # 0xRGB定义成一个整数，前端解析
    base_color = models.IntegerField()
    hover_color = models.IntegerField()
    crowd = models.IntegerField()
    feedback = models.IntegerField() # 1,2,3,4


class Point(models.Model):
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    x = models.DecimalField(decimal_places=10, max_digits=15)
    y = models.DecimalField(decimal_places=10, max_digits=15)
    # crowd 如果crowd为0-30，那么路况为畅通；如果crowd为30-100，那么路况为拥挤；如果crowd为100-200，那么路况为堵塞
