from django.db import models
from users.models import Profile


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='clients_img')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


# for showing 4 recent visited promotions
class UserPromotionVisited(models.Model):
    user = models.ForeignKey(Profile)
    # if user is not authenticated
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    # promotion = models.ForeignKey(Promotion)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
