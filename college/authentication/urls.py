from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.auth)
]
