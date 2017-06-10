from celery import task
import requests


@task()
def fetch_url(url, **kwargs):
    """
    A simple task that fetches the provided URL and returns a tuple
    with the HTTP status code and binary response body (if any)
    """

    r = requests.get(url, **kwargs)
    return (r.status_code, r.content)

@task()
def echo(data):
   """
   A simplest task that just returns back the data it got.
   """
   return data

