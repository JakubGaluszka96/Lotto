from main.models import Bet, LottoDraw
from .models import LottoDraw, Bet, Typing
import datetime

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
    lottoPlus=[]
    wins=int
    winsPlus=int

    def compare(self, draw, bet, plus: bool):
        self.wins=0
        self.winsPlus=0
        self.lotto=[]
        self.lottoPlus=[]
        for i in draw:
            if plus == False:
                if i.isplus == False:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lotto.append(typ)
                        self.wins+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lotto.append(typ)
            if plus == True:
                if i.isplus == False:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lotto.append(typ)
                        self.wins+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lotto.append(typ)
                else:
                    if i.number in bet:
                        typ=Typing(number=i.number, win=True)
                        self.lottoPlus.append(typ)
                        self.winsPlus+=1
                    else:
                        typ=Typing(number=i.number, win=False)
                        self.lottoPlus.append(typ)
        


    def MakeResult(self, draw: LottoDraw, bet: Bet):
        self.id=draw.id
        self.date=draw.date
        lotto = draw.get_typing_list()
        self.compare(draw=lotto, bet=bet.numbers, plus=bet.isplus)
        

class TypeChecker(ResultReport):

    results = []

    def GetDrawsByPeriod (self, bet: Bet):
        start = bet.startdate
        end = bet.enddate
        draws=LottoDraw.objects.filter(date__range=(start, end))
        return draws
    

    def MakeResults(self, bet: Bet):
        draws = self.GetDrawsByPeriod(bet=bet)
        self.results=[]
        for draw in draws:
            result = ResultReport()
            result.MakeResult(draw=draw, bet=bet)
            self.results.append(result)
        



