from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import BetList, Bet
from .forms import CreateNewBet, CheckType, Typing
from .dbupdater import SeleniumDbUpdater
from .typechecker import TypeChecker
# Create your views here.

def index(response, id):
    ls = BetList.objects.get(id=id)
    
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
    ls = BetList.objects.all()
    return render(response, "main/list.html", {"ls":ls})

def update(response):
    Updater=SeleniumDbUpdater()
    Updater.Update()

    return render(response, "main/base.html")


def home(response):
    result = ""
    if response.method == "POST":
        form = CheckType(response.POST)
        if form.is_valid():# and form.is_unique():
            type=Bet()
            type.ParseForm(form=form)
            checker = TypeChecker()
            checker.GetDrawsByPeriod(type)
            result = checker.draws
            
            
        return render(response, "main/home.html", {"form":form, "result":result})
    else:
        form = CheckType()
        return render(response, "main/home.html", {"form":form})



def create(response):
    if response.method == "POST":
        form = CreateNewBet(response.POST)
        print(form)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = BetList(name=n)
            t.save() 
        return HttpResponseRedirect("/%i" %t.id)
        
    else:
        form = CreateNewBet()
        return render(response, "main/create.html", {"form":form})
