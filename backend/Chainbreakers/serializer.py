# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Order, Price, Profile, Transaction


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user_id", "name", "quant", "fiat"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["order_id", "user", "quantity", "buy", "price", "market"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["trans_id", "buyer", "seller",
                  "price", "quant", "buyorder", "sellorder"]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["curr_price", "prev_price"]
