"""
ASGI config for DocsClone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler#DONT USE IN PRODUCTION ONLY DEV!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!(long comment :3c)
import GoogleDocs.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DocsClone.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            GoogleDocs.routing.websocket_urlpatterns
        )
    ),
})