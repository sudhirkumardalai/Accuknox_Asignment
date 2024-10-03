from django.contrib import admin
from django.urls import path
from app3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.signal_test)
]
