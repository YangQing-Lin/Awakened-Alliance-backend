from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.conf import settings
from django.core.cache import cache

class MultiPlayer(AsyncWebsocketConsumer):
    # 前端创建连接的时候调用
    async def connect(self):
        await self.accept()
        print('accept')


    # 前端刷新或者close()时会执行，但不一定（比如电脑突然断电）
    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    # 创建新的玩家时分组，并群发消息
    async def create_player(self, data):
        self.room_name = None
        
        for i in range(1000):
            name = "room-%d" %(i)
            if not cache.has_key(name) or len(cache.get(name)) < settings.ROOM_CAPACITY:
                self.room_name = name
                break
        
        if not self.room_name:
            print("[MY ERROR] do not have enought room name")
            return
        
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
                'type': "group_send_event",
                'event': "create_player",
                'uuid': data['uuid'],
                'username': data['username'],
                'photo': data['photo'],
            }
        )


    async def move_toward(self, data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_send_event",
                'event': "move_toward",
                'uuid': data['uuid'],
                'directions_array': data['directions_array'],
            }
        )


    async def shoot_fireball(self, data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_send_event",
                'event': "shoot_fireball",
                'uuid': data['uuid'],
                'ball_uuid': data['ball_uuid'],
                'tx': data['tx'],
                'ty': data['ty'],
            }
        )


    async def attack(self, data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_send_event",
                'event': "attack",
                'uuid': data['uuid'],
                'attackee_uuid': data['attackee_uuid'],
                'x': data['x'],
                'y': data['y'],
                'angle': data['angle'],
                'damage': data['damage'],
                'ball_uuid': data['ball_uuid'],                
            }
        )


    async def blink(self, data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_send_event",
                'event': "blink",
                'uuid': data['uuid'],
                'tx': data['tx'],
                'ty': data['ty'],
            }
        )


    async def message(self, data):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': "group_send_event",
                'event': "message",
                'uuid': data['uuid'],
                'text': data['text'],
            }
        )


    # 向当前连接的前端发送消息，函数名与'type'关键字保持一致
    # 所有的事件都可以通过调用group_send_event()来实现
    async def group_send_event(self, data):
        await self.send(text_data=json.dumps(data))


    # 接收前端向后端发送的请求
    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        if event == "create_player":
            await self.create_player(data)
        elif event == "move_toward":
            await self.move_toward(data)
        elif event == "shoot_fireball":
            await self.shoot_fireball(data)
        elif event == "attack":
            await self.attack(data)
        elif event == "blink": 
            await self.blink(data)
        elif event == "message":
            await self.message(uuid, data.text)
