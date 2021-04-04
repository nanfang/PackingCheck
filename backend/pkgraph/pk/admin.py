from django.contrib import admin

# Register your models here.
from pk.models import Item, Pack

admin.site.register(Pack)
admin.site.register(Item)
