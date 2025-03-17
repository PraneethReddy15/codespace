from django.contrib import admin
from django.urls import path, include
from morphlelabs import views


urlpatterns = [
    path("",views.htop, name="app")
]
