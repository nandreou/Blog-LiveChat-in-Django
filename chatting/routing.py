from django.urls import re_path
from . import consumers

websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<roomkey>[\w\s]+)/$', consumers.ChatConsumer.as_asgi()),    
    ]
