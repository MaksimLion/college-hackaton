from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('my_account/', views.MyAccountView.as_view()),
    path('my_account/send_report/', views.CreateReport.as_view()),
    path('my_account/labs', views.LabsView.as_view()),
    path('my_account/lab/<int:pk>', views.LabDetail.as_view()),
    path('my_account/labs/statistics', views.LabStatistics.as_view()),

]
