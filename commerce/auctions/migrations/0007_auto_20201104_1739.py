# Generated by Django 3.1.2 on 2020-11-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20201104_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_url',
            field=models.URLField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='listing',
            name='top_bid',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
