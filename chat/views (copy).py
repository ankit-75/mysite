from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .forms import ChatData,ChatDataId
from .models import Chat,Chat_ID
from rest_framework.response import Response
from django.views import generic
import json
import requests
import pprint 
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
	if request.method == 'POST':
		chatData=ChatData(request.POST)
		chatData1=ChatDataId(request.POST)
		if chatData.is_valid():
			chatData.save()
		if chatData1.is_valid():
			chatData1.save()
	return render(request, 'chat/room.html', {
    	'room_name_json':json.dumps(room_name)
    })


def adminchat(request):
	chatid=Chat_ID.objects.all()
	return render(request, 'chat/adminc.html')


# class adminchatdata(APIView):
class adminchatdata(generics.ListAPIView):

	# def adminchatdata(request):
		chatid=Chat_ID.objects.all()
		caa=[]
		for b in chatid:
			caaa={
			'chat_id':b.chat_id,
			'is_active':b.is_active}
			caa.append(caaa)
		data=json.dumps(caa)
		# return render(request,'chat/adminc.html')
