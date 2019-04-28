# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AssetSerializer
from .models import Asset, MarketData
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests


def test(request):
    url = 'http://localhost:8000/api/assets'
    out = requests.get(url).json()
    # out = requests.get(url, data=data).json()
    return JsonResponse(out)


class AssetView2(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class AssetView(generics.ListAPIView):
    serializer_class = AssetSerializer
    serializer_class.Meta = ('name', )

    def get_queryset(self):
        queryset = Asset.objects.all()

        tickers = self.request.query_params.get('ticker', None)
        names = self.request.query_params.get('name', None)

        if (tickers is not None) and (names is None):
            queryset = queryset.filter(ticker__in=tickers.split(','))

        elif (tickers is None) and (names is not None):
            queryset = queryset.filter(name__in=names.split(','))

        return queryset
