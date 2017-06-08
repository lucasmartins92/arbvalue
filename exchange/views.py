from django.shortcuts import render, get_object_or_404
from .models import Exchange

def index(request):
    all_exchanges = Exchange.objects.all()
    return render(request, 'exchange/index.html', {'all_exchanges': all_exchanges})

def detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, exchange_id)
    return render(request, 'exchange/detail.html', {'exchange': exchange})