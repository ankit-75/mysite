from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Chat,Chat_ID
from .serializers import chatmessages,chatonline
from rest_framework import viewsets

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):

	return render(request, 'chat/room.html', {
    	'room_name_json': mark_safe(json.dumps(room_name))
    })


def adminchat(request):
	# chatid=Chat_ID.objects.all()
	# return render(request, 'chat/adminc.html', {"users":chatid})
	return render(request, 'chat/admin.html')

class OnlineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chat_ID.objects.all()
    serializer_class = chatonline
    


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Chat.objects.all()
    serializer_class = chatmessages    