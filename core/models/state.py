from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)


    
