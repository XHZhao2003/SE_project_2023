from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='用户名')
    password = models.CharField(max_length=30, verbose_name='密码')
    # email = models.EmailField(verbose_name='邮箱')
    # # 0:普通用户 1:管理员
    # role = models.IntegerField(default=0, verbose_name='角色')
    # # 0:未删除 1:已删除
    # isDelete = models.IntegerField(default=0, verbose_name='是否删除')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name