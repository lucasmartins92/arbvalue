from celery import shared_task
from .models import Exchange_Pair, Order_Book, Exchange, Currency
from urllib.request import urlopen, Request
from json import load
import time

#================================================================================================
#Check DB

@shared_task
def check_orderbook_db():
    unix_old = time.time()-35*60
    old_data = Order_Book.objects.filter(unix__lte=unix_old)
    print("Quantidade de Dados Antigos: " + str(old_data.count()))
    old_data.delete()

#================================================================================================
#Orderbook

@shared_task
def orderbook_api(url_api):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    neg_order_book = url_api
    req = Request(neg_order_book, headers=headers)
    response = urlopen(req)
    if(response.getcode()==200):
        orderbook = load(response)
        return orderbook

#================================================================================================
#Negocie Coins

@shared_task
def negociecoins_orderbook(url_api, code, base, quote):
    btc_currency = Currency.objects.get(code=base)
    brl_currency = Currency.objects.get(code=quote)
    unix = time.time()
    exchange = Exchange.objects.get(code=code)
    orderbook = orderbook_api(url_api)
    exchange_pair = Exchange_Pair.objects.get(exchange=exchange, base=btc_currency, quote=brl_currency)
    bidbook = orderbook['bid']
    askbook = orderbook['ask']
    count = 1
    for bid in bidbook:
        if count <= 5:
            count += 1
            insert_bid = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='bid',
                                    volume=bid['quantity'],
                                    price=bid['price'])
            insert_bid.save()
        else:
            break
    count = 1
    for ask in askbook:
        if count <= 5:
            count += 1
            insert_ask = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='ask',
                                    volume=ask['quantity'],
                                    price=ask['price'])
            insert_ask.save()
        else:
            break

#================================================================================================
#FoxBit

@shared_task
def foxbit_orderbook(url_api, code, base, quote):
    btc_currency = Currency.objects.get(code=base)
    brl_currency = Currency.objects.get(code=quote)
    unix = time.time()
    exchange = Exchange.objects.get(code=code)
    orderbook = orderbook_api(url_api)
    exchange_pair = Exchange_Pair.objects.get(exchange=exchange, base=btc_currency, quote=brl_currency)
    bidbook = orderbook['bids']
    askbook = orderbook['asks']
    count = 1
    for bid in bidbook:
        if count <= 5:
            count += 1
            insert_bid = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='bid',
                                    volume=bid[1],
                                    price=bid[0])
            insert_bid.save()
        else:
            break
    count = 1
    for ask in askbook:
        if count <= 5:
            count += 1
            insert_ask = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='ask',
                                    volume=ask[1],
                                    price=ask[0])
            insert_ask.save()
        else:
            break

#================================================================================================

@shared_task
def mercadobitcoin_orderbook(url_api, code, base, quote):
    btc_currency = Currency.objects.get(code=base)
    brl_currency = Currency.objects.get(code=quote)
    unix = time.time()
    exchange = Exchange.objects.get(code=code)
    orderbook = orderbook_api(url_api)
    exchange_pair = Exchange_Pair.objects.get(exchange=exchange, base=btc_currency, quote=brl_currency)
    bidbook = orderbook['bids']
    askbook = orderbook['asks']
    count = 1
    for bid in bidbook:
        if count <= 5:
            count += 1
            insert_bid = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='bid',
                                    volume=bid[1],
                                    price=bid[0])
            insert_bid.save()
        else:
            break
    count = 1
    for ask in askbook:
        if count <= 5:
            count += 1
            insert_ask = Order_Book(exchange_pair=exchange_pair,
                                    unix=unix,
                                    type='ask',
                                    volume=ask[1],
                                    price=ask[0])
            insert_ask.save()
        else:
            break

@shared_task
def api():
    check_orderbook_db.delay()
    negociecoins_orderbook.delay("https://broker.negociecoins.com.br/api/v3/BTCBRL/orderbook",
                                 "NEG",
                                 "BTC",
                                 "BRL")
    foxbit_orderbook.delay("https://api.blinktrade.com/api/v1/BRL/orderbook",
                           "FOX",
                           "BTC",
                           "BRL")
    mercadobitcoin_orderbook.delay("https://www.mercadobitcoin.net/api/orderbook/",
                                   "MBT",
                                   "BTC",
                                   "BRL")