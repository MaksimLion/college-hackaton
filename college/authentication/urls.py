from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('sign_in/', views.SignInView.as_view()),
    path('sign_up/', views.SignUpView.as_view()),
]