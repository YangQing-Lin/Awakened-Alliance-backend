from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MultiPlayer(AsyncWebsocketConsumer):
    # 前端创建连接的时候调用
    async def connect(self):
        await self.accept()
        print('accept')

        self.room_name = "room"
        await self.channel_layer.group_add(self.room_name, self.channel_name)


    # 前端刷新或者close()时会执行，但不一定（比如电脑突然断电）
    async def disconnect(self, close_code):
        print('disconnect')
        await self.channel_layer.group_discard(self.room_name, self.channel_name)


    # 接收前端向后端发送的请求
    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
