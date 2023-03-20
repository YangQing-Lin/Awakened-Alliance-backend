from django.db import models
from django.contrib.auth.models import User

# 存储player数据表的信息
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.URLField(max_length=256, blank=True)
    score = models.IntegerField(default=0)
    openid = models.CharField(max_length=50, blank=True, null=True)  # 非必须
    rank_score = models.IntegerField(default=1500)

    # 展示数据的字符串
    def __str__(self):
        return str(self.user) + ' - ' + str(self.score)