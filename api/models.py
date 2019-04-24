from django.db import models

# Create your models here.
class Asset(models.Model):
    ticker = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{name}({ticker})'.format(name=self.name, ticker=self.ticker)


class MarketData(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return '{name} {date}'.format(name=self.asset.name, date=self.date)
