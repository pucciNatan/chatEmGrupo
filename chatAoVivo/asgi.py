import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import meuApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatAoVivo.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            meuApp.routing.websocket_urlpatterns
        )
    )
})

#python -m uvicorn chatAoVivo.asgi:application --port 8000