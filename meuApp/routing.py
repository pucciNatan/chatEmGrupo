from django.urls import path, re_path
from meuApp import consumers

websocket_urlpatterns = [
    re_path(r'ws/app/(?P<nome>\w+)/$', consumers.TesteConsumer.as_asgi()),

]