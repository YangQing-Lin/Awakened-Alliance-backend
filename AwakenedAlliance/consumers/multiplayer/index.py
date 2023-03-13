from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.conf import settings
from django.core.cache import cache

class MultiPlayer(AsyncWebsocketConsumer):
    # 前端创建连接的时候调用
    async def connect(self):
        for i in range(1000):
            name = "room-%d" %(i)
            if not cache.has_key(name) or len(cache.get(name)) < settings.ROOM_CAPACITY:
                self.room_name = name
                break
        
        if not self.room_name:
            print("[MY ERROR] do not have enought room name")
            return
        
        await self.accept()
        print('accept')
        if not cache.has_key(self.room_name):
            cache.set(self.room_name, [], 3600)  # 对战有效期一个小时
        
        # 建立连接之后服务器向本地发送当前所有的玩家信息
        for player in cache.get(self.room_name):
            # json.dumps：将一个json数据结构转换成字符串
            await self.send(text_data=json.dumps({
                'event': "create_player",
                'uuid': player['uuid'],
                'username': player['username'],
                'photo': player['photo'],
            }))

        await self.channel_layer.group_add(self.room_name, self.channel_name)


    # 前端刷新或者close()时会执行，但不一定（比如电脑突然断电）
    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    # 创建新的玩家到组里，并群发消息
    async def create_player(self, data):
        players = cache.get(self.room_name)
        players.append({
            'uuid': data['uuid'],
            'username': data['username'],
            'photo': data['photo'],
        })
        cache.set(self.room_name, players, 3600)
        # 群发消息
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_create_player",
                'event': "create_player",
                'uuid': data['uuid'],
                'username': data['username'],
                'photo': data['photo'],
            }
        )


    # 每个客户端需要有一个函数来接收群发的消息，函数名与'type'关键字保持一致
    async def group_create_player(self, data):
        await self.send(text_data=json.dumps(data))


    # 接收前端向后端发送的请求
    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        if event == "create_player":
            await self.create_player(data)
