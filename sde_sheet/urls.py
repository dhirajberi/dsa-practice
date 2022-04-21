from django.contrib import admin
from django.urls import path
from sde_sheet import views

urlpatterns = [
    path("", views.index, name="home"),
    path("random/<str:ds>", views.random_ds, name="random_ds")
]