from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('app/', views.app),
    path('poetry/', views.poetry),
    path('poetry1/', views.poetry1),
    path('poetry2/', views.poetry2),
    path('dictionary/', views.dictionary),

]
