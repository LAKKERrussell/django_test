from django.db import models

# Create your models here.
from django.utils.html import format_html


class log_move(models.Model):
    ip = models.CharField(max_length = 200)
    ports = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length=200)
    log_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.title


# 权限表
class PowerModel(models.Model):
    user_id = models.CharField(max_length=15, verbose_name='用户ID')
    power = models.CharField(max_length=30, verbose_name='权限')
    team = models.CharField(max_length=30, verbose_name='组别')

    class Meta():
        db_table = 'power'

    def __str__(self):
        return '用户Id：  权限：  组别： '.format(self.user_id, self.power, self.team)


# 用户信息表
class UserInformationModel(models.Model):
    user_id = models.CharField(max_length=15, verbose_name='用户id')
    user_name = models.CharField(max_length=30, verbose_name='用户姓名')
    user_team = models.CharField(max_length=20, verbose_name='用户团队')

    # 取消外键（外键是可用的）
    # stu_course = models.ForeignKey('CourseModel', on_delete=True)
    class Meta():
        db_table = 'userinformation'


# 用户名密码表
class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, verbose_name='用户名')
    password = models.CharField(max_length=10, verbose_name='密码')

    class Meta():
        db_table = 'user'

