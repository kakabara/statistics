from django.contrib import admin
from .models import Locomotive, Mileage, Subsidiary
# Register your models here.

admin.site.register((Locomotive, Mileage, Subsidiary))
