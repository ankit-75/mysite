# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
import requests
from .models import Chat,Chat_ID
# from rasa_core.channels import HttpInputChannel
# from rasa_core.agent import Agent
# from rasa_core.interpreter import RasaNLUInterpreter

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # print("III SSSS")
        # # self.nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
        # # self.agent = Agent.load('./models/dialogue', interpreter = self.nlu_interpreter)
        # print("III EEE")
   

    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.username = self.scope['url_route']['kwargs']['user_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.chatid = None
        #print(self.room_name)
        #print(self.room_group_name)
        #print(self.username)
       # self.channel_name = 'specific.WAjyBVrd!kcRtvGyJBIqh'
       # print(self.channel_name) 
        print("USER NAME {} CHANNEL NAME {}".format(self.username,self.channel_name))

        #self.nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
        #self.agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

       

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        #print("ACCEPT")

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        if(self.chatid != None):
            Chat_ID.objects.filter(chatid = self.chatid).update(is_active= False)
    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.chatid = text_data_json['chatid']
        print("RECV {}".format(text_data_json))
        # res = self.agent.handle_message(message);
        # print(res)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'reply': False,
                'chatid':self.chatid,
                'channel_name': self.channel_name
            }
        )

        
        Chat_ID.objects.get_or_create(chatid=self.chatid ,roomname=self.room_group_name ,is_active=True, username = self.username,channel_name= self.channel_name)
        Chat.objects.create(chatid=self.chatid , roomname=self.room_group_name ,messagedata=message, user_msg = 1)
        try:
            with requests.Session() as sess:
                url = 'http://localhost:5004/webhook'

                # Set user-agent and auth headers
                sess.headers = {
                    'Content-type': 'application/json',
                    'Authorization': 'Bearer'
                }
                
                post_data =  {
                    'sender': self.room_name, 
                    'message': message,
                    'chatid' :self.chatid,
                    'channel_name': self.channel_name
                }

               
                # Submit the request
                sess.post(
                    url,
                    #headers=headers,
                    data=json.dumps(post_data),
                    files=None,
                    timeout=None,
                    proxies=None
                )
        except Exception as e:
            print(e)
        
        #Chat_ID.objects.get_or_create(chat_id=self.room_group_name,is_active=True)

    # Receive message from room group
    def chat_message(self, event):
        print('CHAT MESSAGE {}'.format(event))
        #message = event['message']

        #Send message to WebSocket
        self.send(text_data=json.dumps({
            'response': event
        }))


# from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from .models import Chat,Chat_ID


# class ChatConsumer(AsyncWebsocketConsumer):
#     it = 0

#     async def connect(self):

#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         # Join room group
#         self.room_group_name='chat_admin'
#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         if (self.it!=0):
#             Chat_ID.objects.filter(chat_id = self.it).update(is_active= False)
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         it2 = text_data_json['it2']
#         self.it = text_data_json['it']
#         if (it2==0):
#             Chat.objects.create(chatid=self.it,messagedata=message)
#             Chat_ID.objects.get_or_create(chat_id=self.it,is_active=True)
#         # Send message to room group
#         await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'chat_message',
#                     'message': message,
#                     'it2': it2,
#                     'it':self.it
#                 }
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event['message']
#         it = event['it']
#         it2 = event['it2']
#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({
#                 'message': message,
#                 'it':it,
#                 'it2':it2
#             }))