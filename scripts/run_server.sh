#! /bin/bash

# python3 /home/aa/GraduationProject/manage.py runserver 0.0.0.0:8000

# 更新数据库结构(之后写游戏的时候可以注释掉，只有需要的时候才调用)
# ./register_database.sh

# 归档静态文件
echo yes | python3 /home/aa/GraduationProject/manage.py collectstatic

uwsgi --ini /home/aa/GraduationProject/scripts/uwsgi.ini
# 我



# 记录一下这里的坑点，项目进行到这里已经需要多个服务了，顺序是：
# 启动nginx服务             sudo /etc/init.d/nginx start
# 启动redis-server服务      sudo redis-server /etc/redis/redis.conf
# 重启redis服务             sudo /etc/init.d/redis-server restart
# 启动uwsgi服务             uwsgi –-ini scripts/uwsgi.ini
# 启动django_channels服务   daphne -b 0.0.0.0 -p 5015 acapp.asgi:application
# 启动匹配系统              （在match_system/src目录下） ./main.py

# pip uninstall channels-redis
# pip install channels-redis==3.4.1

# from django.core.cache import cache
# def clear():
#     for key in cache.keys('*'):
#         cache.delete(key)

# django使用mysql数据库，并从db.sqlite3迁移数据的方法：
# https://blog.csdn.net/DahlinSky/article/details/104467237
# https://blog.csdn.net/YPL_ZML/article/details/91892306

# Linux下修改文件编码为unix
# vim进入文件   :set ff=unix
# VS Code修改文件为unix
# Ctrl+, 搜索eol 修改第一项为\n
# 之后新建的文件都是unix编码，但是已经存在的文件不会改变