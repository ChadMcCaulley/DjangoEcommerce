# Generated by Django 3.0.8 on 2020-10-07 01:26

import core.datatypes
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20200925_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=core.datatypes.NullableForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=core.datatypes.NullableForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment', to='core.Payment'),
        ),
    ]