# Generated by Django 3.0.8 on 2020-08-06 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200806_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemimage',
            name='title',
        ),
    ]
