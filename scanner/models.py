from django.db import models

# Create your models here.
class Receipt(models.Model):
    store = models.CharField(max_length=200)
    total_price = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tax_rate = models.FloatField(default=0)

    def __str__(self):
        return self.store


class Item(models.Model):
    receipt_id = models.IntegerField()
    item = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.item
