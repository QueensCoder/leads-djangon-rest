from django.db import models


class Pets(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
