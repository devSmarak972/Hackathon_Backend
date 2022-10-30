from django.contrib import admin
from .models import Profile, Order, Transaction, Price
from django.contrib import admin
# Register your models here.


admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Price)
