from django.db import models
from datetime import datetime


# 員工帳號
class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=100)
    status = models.IntegerField(default=1)    #狀態:1正常/2禁用/6管理員/9删除
    create_at = models.DateTimeField(default=datetime.now)    #創建时间
    update_at = models.DateTimeField(default=datetime.now)    #修改时间