from django.contrib import admin
from .models import Item, Invoice

# Register your models here.
admin.site.register(Item)
admin.site.register(Invoice)
