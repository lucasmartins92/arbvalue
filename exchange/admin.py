from django.contrib import admin
from .models import Exchange, Currency, Exchange_Currency, Exchange_Pair

admin.site.register(Exchange)
admin.site.register(Currency)
admin.site.register(Exchange_Currency)
admin.site.register(Exchange_Pair)