
from django.contrib import admin
from django.urls import path
from .views import Dharma
urlpatterns = [
    path('',Dharma),
]
