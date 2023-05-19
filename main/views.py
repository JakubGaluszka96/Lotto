from django.shortcuts import render
from django.http import HttpResponse
from .models import TypesList, Type
# Create your views here.

def index(response, id):
    ls = TypesList.objects.get(id=id)
    typ = ls.type_set.get()
    return HttpResponse("Welcome to Lotto checker site %s %s" % (ls.name, typ.typing))


