# Generated by Django 3.1.2 on 2020-11-06 00:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20201105_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='wishlisted_listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
