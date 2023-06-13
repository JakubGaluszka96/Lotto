from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TypesList, Type
from .forms import CreateNewType, CheckType
# Create your views here.

def index(response, id):
    ls = TypesList.objects.get(id=id)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for type in ls.type_set.all():
                print(response.POST.get("c" + str(type.id)))
                if response.POST.get("c" + str(type.id)) == "clicked":
                    type.winner=True
                else:
                    type.winner=False
                type.save()
        elif response.POST.get("newType"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.type_set.create(typing=txt, winner=False)
            else:
                print("invalid input")
            

    return render(response, "main/type.html", {"ls":ls})

def list(response):
    ls = TypesList.objects.all()
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    lista = [x for x in range(1,50)]
    number = [x for x in range(0,6)]
    if response.method == "POST":
        form = CheckType(response.POST)
        if form.is_valid():
            n1=form.cleaned_data["number1"]
        return HttpResponseRedirect("/#")
    else:
        form = CheckType()
        return render(response, "main/home.html", {"form":form, "range" :lista, "number":number})

def create(response):
    if response.method == "POST":
        form = CreateNewType(response.POST)
        print(form)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TypesList(name=n)
            t.save() 
        return HttpResponseRedirect("/%i" %t.id)
        
    else:
        form = CreateNewType()
        return render(response, "main/create.html", {"form":form})
