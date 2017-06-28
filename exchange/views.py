from django.shortcuts import render, get_object_or_404
from exchange.models import Exchange, Exchange_Pair, Order_Book

def index(request):
    all_exchanges = Exchange.objects.all()
    return render(request, 'base.html', {'all_exchanges': all_exchanges})

def detail(request, exchange_id):
    exchange = get_object_or_404(Exchange, pk=exchange_id)
    return render(request, 'exchange/detail.html',
                  {'exchange': exchange},
                  )
'''
#================ tutorial ===============================================

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from exchange.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
'''