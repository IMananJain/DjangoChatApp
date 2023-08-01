# This code is configuring the ASGI (Asynchronous Server Gateway Interface) application for a Django
# project that uses Channels for handling WebSocket connections.
import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

# The `application` variable is being assigned a `ProtocolTypeRouter` object. This object is
# responsible for routing incoming requests to the appropriate protocol-specific application.
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})