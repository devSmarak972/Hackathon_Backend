from django.contrib import admin
from .models import Profile, Order, Transaction
from django.contrib import admin
# Register your models here.


admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Transaction)