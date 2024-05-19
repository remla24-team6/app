from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("check/", views.check, name="check"),
    path("add_training/", views.add_training, name="add_training"),
]