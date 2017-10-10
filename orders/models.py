from django.db import models
from promotions.models import Coupon


# Create your models here.

class Order(models.Model):
    price_discounted = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class CouponInOrder(models.Model):
    coupon = models.ForeignKey(Coupon)
    nmb = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    price_per_item_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
