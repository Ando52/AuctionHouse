# Generated by Django 3.1.2 on 2020-11-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201104_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='win',
            field=models.IntegerField(default=0),
        ),
    ]
