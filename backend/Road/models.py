from django.db import models

class Road(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # 前端定义折线的节点数量，规定最大不超过4
    num_of_points = models.IntegerField()
    point_1x = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_1y = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_2x = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_2y = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_3x = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_3y = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_4x = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    point_4y = models.DecimalField(decimal_places=10, max_digits=15, default=0)
    # 0xRGB定义成一个整数，前端解析
    base_color = models.IntegerField()
    hover_color = models.IntegerField()
    
    feedback_1 = models.IntegerField()
    feedback_2 = models.IntegerField()
    feedback_3 = models.IntegerField()
    feedback_4 = models.IntegerField()
    # crowd
    
