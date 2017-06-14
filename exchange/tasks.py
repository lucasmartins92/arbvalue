from celery import shared_task
from .models import Exchange_Pair, Order_Book, Exchange, Currency
from urllib.request import urlopen, Request
from json import load
import time

#================================================================================================
#Negocie Coins
@shared_task
def negociecoins_orderbook():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    neg_order_book = "https://broker.negociecoins.com.br/api/v3/BTCBRL/orderbook"
    req = Request(neg_order_book, headers=headers)
    response = urlopen(req)
    if(response.getcode()==200):
        orderbook = load(response)
        unix = time.time()
        exchange = Exchange.objects.get(code="NEG")
        base = Currency.objects.get(code="BTC")
        quote = Currency.objects.get(code="BRL")
        exchange_pair = Exchange_Pair.objects.get(exchange=exchange, base=base, quote=quote)
        insert_negociecoins_db(exchange_pair, unix, orderbook)
@shared_task
def insert_negociecoins_db(exchange_pair, unix, orderbook):
    Exchange_Pair.objects.filter()
    bidbook = orderbook['bid']
    askbook = orderbook['ask']
    for bid in bidbook:
        insert_bid = Order_Book(exchange_pair=exchange_pair,
                                unix=unix,
                                type='bid',
                                volume=bid['quantity'],
                                price=bid['price'])
        insert_bid.save()
    for ask in askbook:
        insert_ask = Order_Book(exchange_pair=exchange_pair,
                                unix=unix,
                                type='ask',
                                volume=ask['quantity'],
                                price=ask['price'])
        insert_ask.save()
#================================================================================================

@shared_task
def api():
    negociecoins_orderbook.delay()