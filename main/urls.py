from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>",views.index, name="index"),
    path("list/",views.list, name="list"),
    path("create/",views.create, name="create"),
    path("update/",views.update, name="update"),
    path("", views.home, name="home"),
    ]