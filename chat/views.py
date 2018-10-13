from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Chat,Chat_ID
from .serializers import chatmessages,chatonline
from rest_framework import viewsets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
import time
#from channels import Channel

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    #channel_layer = get_channel_layer()
    #print(channel_layer)
	return render(request, 'chat/room.html', {
    	'name_json': mark_safe(json.dumps(room_name))
    })


def adminchat(request):
	# chatid=Chat_ID.objects.all()
	# return render(request, 'chat/adminc.html', {"users":chatid})
	return render(request, 'chat/admin.html')
def list(request):
    channel_layer = get_channel_layer()
    print(channel_layer)

    async_to_sync(channel_layer.group_send)(
            "chat_abc",
            {
                'type': 'chat_message',
                'message': "asdfasfdasdsdfgsdfgsdfg"
            }
        )

    return HttpResponse("return this string")

def postreq(request):
    #print(request)
    req = json.dumps(request.POST)#request.POST.get('message', '')
    print("REQ {}".format(req))
    #print(req)
    text = request.POST.get('text', '')
    sender_id       = request.POST.get('sender_id', '')
    chatid          = request.POST.get('chatid', '')
    channel_name    = request.POST.get('channel_name', '')
    channel_layer   = get_channel_layer()
    print(channel_layer);
    #print(self.channel_layer);

    room_group_name = "chat_"+sender_id

    time.sleep(2)
    async_to_sync(channel_layer.group_send)(
            room_group_name,
            {
                'type': 'chat_message',
                'response': text,
                "reply" : True,
                "chatid":chatid
            }
        )
     # async_to_sync(channel_layer.group_send)(
     #        room_group_name,
     #        {
     #            'type': 'chat_message',
     #            'response': text,
     #            "reply" : True,
     #            "chatid":chatid
     #        }
     #    )
    Chat.objects.create(chatid=chatid, roomname=room_group_name ,messagedata=text, user_msg = 0)
    return HttpResponse("success")


class OnlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chat_ID.objects.all()
    #formatt = self.request.query_params.get('format')
    #print(formatt)
    serializer_class = chatonline

    def filter_queryset(self, queryset):
        
        queryset = Chat_ID.objects.filter(is_active=1)

        return queryset


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = chatmessages  

    # def get_queryset(self):
    #     #queryset = Chat.objects.filter(chatid="1536385520641")
    #     #print(queryset)
    #     return queryset 
    def filter_queryset(self, queryset):
        # filter_backends = (CategoryFilter,)

        # if 'geo_route' in self.request.query_params:
        #     filter_backends = (GeoRouteFilter, CategoryFilter)
        # elif 'geo_point' in self.request.query_params:
        #     filter_backends = (GeoPointFilter, CategoryFilter)

        # for backend in list(filter_backends):
        #     queryset = backend().filter_queryset(self.request, queryset, view=self)
        chatid = self.request.GET.get('id')
        print(chatid)

        queryset = Chat.objects.filter(chatid=chatid)

        return queryset