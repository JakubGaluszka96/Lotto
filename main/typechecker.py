from main.models import UserBet, LottoDraw
from .models import LottoDraw, UserBet, Typing
from .forms import CheckType
import datetime
import json

class Bet():
    startdate = datetime
    enddate = datetime
    is_plus = bool
    numbers = []

    def parse_form(self, form: CheckType):
        self.startdate=form.cleaned_data["startdate"]
        self.enddate=form.cleaned_data["enddate"]
        self.is_plus=form.cleaned_data["isplus"]
        self.numbers = [form.cleaned_data["number1"], 
                   form.cleaned_data["number2"], 
                   form.cleaned_data["number3"], 
                   form.cleaned_data["number4"], 
                   form.cleaned_data["number5"], 
                   form.cleaned_data["number6"]]

    def parse_userbet(self, bet: UserBet):
        self.startdate=bet.startdate
        self.enddate=bet.enddate
        self.is_plus=bet.is_plus
        self.numbers = bet.get_numbers()

class Typing():
    number=int
    win=bool
    def __init__ (self, number: int, win:bool):
        self.number=number
        self.win=win

class ResultReport():
    id=int
    date=datetime.date
    lotto=[]
    lotto_plus=[]
    wins=int
    wins_plus=int

    def compare(self, draw, bet, plus: bool):
        self.wins=0
        self.wins_plus=None
        self.lotto=[]
        self.lotto_plus=[]
        for i in draw:
            if plus == False:
                if i.is_plus == False:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lotto.append(typ)
                        self.wins+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lotto.append(typ)
            if plus == True:
                if i.is_plus == False:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lotto.append(typ)
                        self.wins+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lotto.append(typ)
                elif i.is_plus == True:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lotto_plus.append(typ)
                        if self.wins_plus == None:
                            self.wins_plus = 1
                        else:
                            self.wins_plus+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lotto_plus.append(typ)
                        if self.wins_plus == None:
                            self.wins_plus = 0
        


    def make_result(self, draw: LottoDraw, bet: Bet):
        self.id=draw.id
        self.date=draw.date
        lotto = draw.get_typing_list()
        self.compare(draw=lotto, bet=bet.numbers, plus=bet.is_plus)
        

class TypeChecker(ResultReport):

    results = []

    def get_draws_by_period (self, bet: Bet):
        start = bet.startdate
        end = bet.enddate
        draws=LottoDraw.objects.filter(date__range=(start, end))
        return draws
    

    def make_results(self, bet: Bet):
        draws = self.get_draws_by_period(bet=bet)
        self.results=[]
        for draw in draws:
            result = ResultReport()
            result.make_result(draw=draw, bet=bet)
            self.results.append(result)


    def get_summary(self):
        output={"lotto":{},
                "lotto_plus":{}}
        
        summary = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0
                   }
        for i in self.results:
            for j in summary:
                key = j
                if i.wins==j:
                    summary[key]+=1
        output["lotto"]=summary


        summary = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 0,
                   6: 0
                   }
        for i in self.results:
            for j in summary:
                key = j
                if i.wins_plus==j:
                    summary[key]+=1
        output["lotto_plus"]=summary
        output_json = json.dumps(output)
        
        return output_json


        



