from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Welcome to Lotto checker site")

def v1(response):
    return HttpResponse("Welcome to Lotver site")
