from django.urls import path
from meuApp import consumers

websocket_urlpatterns = [
    path('ws/app/', consumers.TesteConsumer.as_asgi()),
]