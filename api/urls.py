from django.urls import path, include
from rest_framework import routers

from api import views

urlpatterns = [
    path('webhook/', views.webhook),
]