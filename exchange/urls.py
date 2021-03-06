from django.conf.urls import url, include
from . import views

app_name = 'exchange'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<exchange_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^prices/$', views.prices, name='prices'),
]
