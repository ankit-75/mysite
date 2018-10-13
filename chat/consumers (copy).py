from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Chat,Chat_ID


class ChatConsumer(AsyncWebsocketConsumer):
    it = 0

    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        self.room_group_name='chat_admin'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        if (self.it!=0):
            Chat_ID.objects.filter(chat_id = self.it).update(is_active= False)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        it2 = text_data_json['it2']
        self.it = text_data_json['it']
        if (it2==0):
            Chat.objects.create(chatid=self.it,messagedata=message)
            Chat_ID.objects.get_or_create(chat_id=self.it,is_active=True)
        # Send message to room group
        await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'it2': it2,
                    'it':self.it
                }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        it = event['it']
        it2 = event['it2']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
                'message': message,
                'it':it,
                'it2':it2
            }))