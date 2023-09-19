from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseServerError
import json

def aityping(response):
        return render(response, "aityping/aityping.html")