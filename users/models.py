from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    purchases_nmb = models.DecimalField(max_digits=2, decimal_places=0)
