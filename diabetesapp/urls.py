from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor),
    path('', views.formInfo, name='index'),
    path('result', views.formInfo, name='result'),
]
