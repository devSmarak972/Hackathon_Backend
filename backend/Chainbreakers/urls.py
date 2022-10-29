# todo/todo_api/urls.py : API urls.py
# from django.conf.urls import url
from django.urls import path, include,re_path
from .views import (
    ProfileView, OrderView, TransactionView,
)

urlpatterns = [
    re_path(r'^api/profile', ProfileView.as_view()),
    re_path(r'^api/order', OrderView.as_view()),
    re_path(r'^api/transaction', TransactionView.as_view()),
]