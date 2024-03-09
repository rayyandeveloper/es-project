
import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

from chat import urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(urls.websocket_urlpatterns),
})