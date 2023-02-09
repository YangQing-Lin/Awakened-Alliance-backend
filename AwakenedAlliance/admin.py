from django.contrib import admin
from AwakenedAlliance.models.player.player import Player

# 将修改的数据库表注册到数据库中
admin.site.register(Player)