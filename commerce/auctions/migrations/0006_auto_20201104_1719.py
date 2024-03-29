# Generated by Django 3.1.2 on 2020-11-04 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201104_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='listing',
            name='top_bid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
