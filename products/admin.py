from django.contrib import admin

# Register your models here.
from .models import Product

# Lets the admin site know about products
admin.site.register(Product)
