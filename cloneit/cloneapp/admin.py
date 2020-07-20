from django.contrib import admin
from .models import Products,Cartitem,Userprofile

# Register your models here.
admin.site.register(Products)
admin.site.register(Cartitem)
admin.site.register(Userprofile)
