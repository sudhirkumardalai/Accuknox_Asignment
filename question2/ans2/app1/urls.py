# myproject/urls.py
from django.contrib import admin
from django.urls import path
from .views import create_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', create_model, name='create_model'),
]
