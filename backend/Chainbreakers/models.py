# backend/Chainbreakers/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default='Unknown')
    quant = models.IntegerField(default=0)
    fiat = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    # timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    quantity = models.IntegerField(default=0)
    buy = models.BooleanField()
    # True==buy False==sell
    price = models.FloatField(default=0)
    market = models.BooleanField()
    # True==market order Falselimit order

    # def __str__(self):
    #     return self.order_id


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='buyer', null=True, blank=True)
    seller = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='seller', null=True, blank=True)
    price = models.FloatField(default=0)
    quant = models.IntegerField(default=0)
    buyorder = models.IntegerField(default=0)
    sellorder = models.IntegerField(default=0)

    def __str__(self):
        return str(self.buyer)+" "+str(self.seller)


class Price(models.Model):
    curr_price = models.FloatField()
    prev_price = models.FloatField()
    step = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.curr_price)
