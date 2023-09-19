from django.urls import path
from . import views

urlpatterns = [
    path("", views.aityping, name="aityping"),
]