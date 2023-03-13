#! /bin/bash

# python3 /home/aa/GraduationProject/manage.py runserver 0.0.0.0:8000

# 更新数据库结构(之后写游戏的时候可以注释掉，只有需要的时候才调用)
./register_database.sh

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
