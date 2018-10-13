# chat/urls.py
from django.conf.urls import url

from . import views
app_name=""
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^adminchat/$', views.adminchat, name='adminchat'),
    url(r'^list/$', views.list),
    url(r'^postreq/$', views.postreq),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]