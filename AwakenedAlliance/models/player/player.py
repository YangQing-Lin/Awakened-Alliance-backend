from django.db import models
from django.contrib.auth.models import User

# 存储player数据表的信息
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)

    # 展示数据的字符串
    def __str__(self):
        return str(self.user)