# Generated by Django 3.0.8 on 2020-07-24 06:09

import core.datatypes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200724_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='max_price',
            field=core.datatypes.NullableDecimal(blank=True, decimal_places=2, default=None, editable=False, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='min_price',
            field=core.datatypes.NullableDecimal(blank=True, decimal_places=2, default=None, editable=False, max_digits=15, null=True),
        ),
    ]