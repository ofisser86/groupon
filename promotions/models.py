import uuid as uuid
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # can be null if it is top level category
    category_one = models.ForeignKey('self', related_name="Category One")

    # can be null if it is top level category
    category_two = models.ForeignKey('self', related_name="Category One")

    # can be null if it is top level category
    category_three = models.ForeignKey('self', related_name="Category One")

    # active promotions nmb
    promotions_nmb = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Promotion(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    faq = models.TextField(blank=True, null=True, default=None)
    what_you_get = models.TextField(blank=True, null=True, default=None)
    # coordinates in longtitude and latitude
    map = models.CharField(max_length=32, blank=True, null=True, default=None)

    category = models.ForeignKey('Category')
    address = models.CharField(max_length=128, blank=True, null=True, default=None)
    coordinates_latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    coordinates_longtitude = models.DecimalField(max_digits=8, decimal_places=6, default=0)
    # date time when this promotion will be expired
    dt_expiration = models.DateTimeField(auto_now=False, auto_now_add=False)
    rating_total = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    review_nmb = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    purchases_nmb = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    is_top_seller = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    # Slug for SEO URL
    slug = models.SlugField(max_length=50)


class PromotionImage(models.Model):
    promotion = models.ForeignKey('Promotion')
    image = models.ImageField(upload_to='promotions_img')
    is_main = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class Coupon(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    promotion = models.ForeignKey('Promotions')
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    price_initial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_discounted = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_rate = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    purchases_nmb = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TYPE_OF_DISCOUNT = (('A', 'All'), ('C', 'Clearance'))

    discount_type = models.CharField(max_length=2, choices=TYPE_OF_DISCOUNT)


class ReviewItem(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category')


class Review(models.Model):
    promotion = models.ForeignKey(Promotion)
    user = models.ForeignKey('User')
    text = models.TextField()
    # calculated field
    rating_total = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    is_verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class ReviewItemScore(models.Model):
    review = models.ForeignKey('Review')
    review_item = models.ForeignKey('ReviewItem')
    rating = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    comment = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
