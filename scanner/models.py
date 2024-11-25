from django.db import models


class Receipt(models.Model):
    # per receipt attribute
    store = models.CharField(max_length=200)
    total_price = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tax_rate = models.FloatField(default=0)
    photo_id = models.IntegerField(default=0)

    def __str__(self):
        return self.store


class Item(models.Model):
    # item attribute
    receipt_id = models.IntegerField()
    item = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.item


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo {self.id} uploaded at {self.uploaded_at}"
