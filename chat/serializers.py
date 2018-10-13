from rest_framework import serializers
from chat.models import Chat,Chat_ID

class chatmessages(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = ('messagedata', 'user_msg')


class chatonline(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat_ID
        fields = ('chatid', 'is_active',"username")