from django.contrib import admin
from django.apps import apps

models = apps.all_models['core']

for model in models.values():
    admin.site.register(model)