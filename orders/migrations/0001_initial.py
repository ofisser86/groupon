# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('price_per_item_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_total_discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotions.Coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_discounted', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]