from django.shortcuts import render, render_to_response, get_object_or_404
from exchange.models import Exchange, Exchange_Pair, Order_Book
import json
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie


def loan(request):
    return render(request, 'loan.html')


def index(request):
    all_exchanges = Exchange.objects.all()
    return render(request, 'home.html', {'all_exchanges': all_exchanges})


def detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    return render(request, 'exchange/detail.html',
                  {'exchange': exchange},
                  )


def prices(request):
    if request.method == 'GET':
        exchange_id = request.GET.get('exchange_id')
        exchange = get_object_or_404(Exchange, pk=exchange_id)
        return render_to_response('exchange/prices.html', {'exchange': exchange})
    else:
        exchange_id = request.POST.get('exchange_id')
        exchange = get_object_or_404(Exchange, pk=exchange_id)
        return render_to_response('exchange/prices.html', {'exchange': exchange})
