from django.db import models
import django

# Create your models here.
class Exchange(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return "(" + self.code + ")" + self.name


class Currency(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return "(" + self.code + ") " + self.name

class Exchange_Currency(models.Model):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    deposit_percent = models.DecimalField(max_digits=30, decimal_places=10)
    deposit_value = models.DecimalField(max_digits=30, decimal_places=10)
    withdraw_percent = models.DecimalField(max_digits=30, decimal_places=10)
    withdraw_value = models.DecimalField(max_digits=30, decimal_places=10)

    def __str__(self):
        return str(self.exchange) + " - " + str(self.currency)

class Exchange_Pair(models.Model):
    base = models.ForeignKey(Currency, related_name="base_currency", on_delete=models.CASCADE)
    quote = models.ForeignKey(Currency, related_name="quote_currency", on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, default='', on_delete=models.CASCADE)
    book_order_percent = models.DecimalField(max_digits=30, decimal_places=10)
    book_order_value = models.DecimalField(max_digits=30, decimal_places=10)
    market_order_percent = models.DecimalField(max_digits=30, decimal_places=10)
    market_order_value = models.DecimalField(max_digits=25, decimal_places=10)

    def __str__(self):
        return str(self.exchange) + ": " + str(self.base) + "/" + str(self.quote)