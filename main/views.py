from django.shortcuts import render
from django.http import HttpResponse
from .models import TypesList, Type
from .forms import CreateNewType
# Create your views here.

def index(response, id):
    ls = TypesList.objects.get(id=id)
    return render(response, "main/type.html", {"ls":ls})

def list(response):
    ls = TypesList.objects.all()
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    form = CreateNewType()
    return render(response, "main/create.html", {"form":form})
