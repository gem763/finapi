from django.contrib import admin
from .models import Asset, MarketData

# Register your models here.
admin.site.register(Asset)
admin.site.register(MarketData)
