from celery import shared_task
import requests
from urllib.request import urlopen, Request
from json import load
from .models import TaskHistory
import time

#celery = Celery('tasks', broker='redis://localhost:6379/0')

@shared_task()
def fetch_url(url, **kwargs):
    """
    A simple task that fetches the provided URL and returns a tuple
    with the HTTP status code and binary response body (if any)
    """

    r = requests.get(url, **kwargs)
    return (r.status_code, r.content)

@shared_task()
def echo(data):
   """
   A simplest task that just returns back the data it got.
   """
   return data

@shared_task
def api_orderbook():
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    neg_order_book = "https://broker.negociecoins.com.br/api/v3/btcbrl/ticker"
    req = Request(neg_order_book, headers=headers)
    response = urlopen(req)
    data = load(response)
    return data

@shared_task
def insert_orderbook_sqlite(unix):
    order_book = api_orderbook()
    bid = order_book['buy']
    ask = order_book['sell']


@shared_task
def api():
    print("Api_beginning")
    api = TaskHistory()
    api.name = "api"
    api.unix = time.time()
    api.save()
    print("Api_end")