from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from authentication import views

urlpatterns = [
    #path('', views.sign_up),
    path('sign_in/', views.sign_in),
    path('sign_up/', views.sign_up),
    path('my_account/', views.my_account),
    path('logout/', views.logout_view)
]
