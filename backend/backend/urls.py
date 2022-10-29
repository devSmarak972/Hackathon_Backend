# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from Chainbreakers import urls as app_urls
from Chainbreakers.views import create_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(app_urls)),
    # path('', create_user),
]