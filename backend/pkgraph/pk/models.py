from django.contrib.auth.models import User
from django.db import models


# from django.auth im
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=256)


class Pack(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=256)
    items = models.ManyToManyField(Item, blank=True)
