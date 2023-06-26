from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("species/<int:pk>", views.dog_spiceis, name="dog_spiceis"),
]
