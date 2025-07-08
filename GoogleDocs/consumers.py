import json
from channels.generic.websocket import AsyncWebsocketConsumer
#consumers.py = django views but for channels/websockets, can request info recive and send
class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.room_group_name = f'document_{self.doc_id}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_update',
                'message': message,
                'sender': self.channel_name  # Add sender tag
            }
        )

    async def send_update(self, event):
        # Prevent sender from receiving their own message
        if event['sender'] == self.channel_name:
            return

        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
