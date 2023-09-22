from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http.response import HttpResponseServerError

import json

def aityping(response):
        header = ['id', 'date', 'number1', 'number2', 'number3', 'number4', 'number5', 'number6']
        return render(response, "aityping/aityping.html")



