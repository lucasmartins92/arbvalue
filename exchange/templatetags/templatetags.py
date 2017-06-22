from django.template import Library
from django.db.models import Max
from pytz import timezone, UTC
from datetime import datetime


register = Library()

@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter
def sort_by(queryset, order):
    return queryset.order_by(order)

@register.filter
def filter_order_by(queryset, order):
    max_unix = queryset.aggregate(Max('unix'))
    filtered = queryset.filter(unix=max_unix['unix__max'])
    return filtered.order_by(order)

@register.filter
def timestamp(timestamp_br):
    try:
        ts = datetime.fromtimestamp(timestamp)
    except ValueError:
        return None
    return ts.replace(tzinfo=UTC).astimezone(timezone('America/Sao_Paulo')).strftime("%H:%M:%S")