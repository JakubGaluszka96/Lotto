from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,BadHeaderError
from .models import LottoDraw, UserBet, Number
from .forms import CreateNewBet, CheckType
from .dbupdater import SeleniumDbUpdater
from .typechecker import TypeChecker, ResultReport, Typing, Bet
from django.http.response import HttpResponseServerError
import json
# Create your views here.

def index(response, id):
    userbet = UserBet.objects.get(id=id)
    if userbet in response.user.userbet.all():
        bet=Bet()
        bet.parse_userbet(bet=userbet)
        checker = TypeChecker()
        checker.make_results(bet)
        results = checker.results
        summary = json.loads(checker.get_summary())
        return render(response, "main/result.html", {"results":results, "summary":summary})
    else:
        return HttpResponseServerError("<h>500</h><p>Incorrect user</p>")
            


def list(response):
    bet_list = response.user.userbet.all()
    return render(response, "main/list.html", {"bet_list":bet_list})

def update(response):
    updater=SeleniumDbUpdater()
    updater.update()

    return render(response, "main/base.html")


def home(response):
    if response.method == "POST":
        form = CheckType(response.POST)
        if form.is_valid():# and form.is_unique():
            bet=Bet()
            bet.parse_form(form=form)
            checker = TypeChecker()
            checker.make_results(bet)
            results = checker.results
            summary = json.loads(checker.get_summary())
        return render(response, "main/home.html", {"form":form, "results":results, "summary":summary})
    else:
        form = CheckType()
        return render(response, "main/home.html", {"form":form})



def create(response):
    if response.method == "POST":
        form = CreateNewBet(response.POST)
        if form.is_valid():
            user_bet=UserBet(name=form.cleaned_data["name"],
                             startdate=form.cleaned_data["startdate"],
                             enddate=form.cleaned_data["enddate"],
                             is_plus=form.cleaned_data["isplus"])
            user_bet.save()
            id = user_bet.id
            response.user.userbet.add(user_bet)
            user_bet=UserBet.objects.get(id=id)
            numbers = [form.cleaned_data["number1"], 
                   form.cleaned_data["number2"], 
                   form.cleaned_data["number3"], 
                   form.cleaned_data["number4"], 
                   form.cleaned_data["number5"], 
                   form.cleaned_data["number6"]]
            for i in numbers:           
                user_bet.number_set.create(number=i, win=False)

                

        return HttpResponseRedirect("/list")#"/%i" %bet.id)
        
    else:
        form = CreateNewBet()
        return render(response, "main/create.html", {"form":form})

