# Generated by Django 3.1.2 on 2020-11-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20201106_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.CharField(default='11/6/2020', max_length=10),
        ),
    ]
