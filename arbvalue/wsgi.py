"""
WSGI config for arbvalue project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "arbvalue.settings")

application = get_wsgi_application()

from exchange.models import Exchange_Currency, Exchange_Pair, Exchange, Currency

exchange = Exchange.objects.all()
Currency = Currency.objects.all()

print(exchange)
