from main.models import Bet, LottoDraw
from .models import LottoDraw, Bet, Typing
import datetime

class Typing():
    number=int
    win=bool

class ResultReport():
    id=int
    date=datetime.date
    lotto=[Typing]
    lottoPlus=[Typing]
    wins=int
    winsPlus=int

    def Compare(self, draw, bet, plus: bool):
        self.wins=0
        self.winsPlus=0
        for i in draw:
            if plus == False:
                if any(bet) == i:
                    self.lotto.append(Typing(number=i, win=True))
                    self.wins+=1
            if plus == True:
                if any(bet) != i:
                    self.lottoPlus.append(Typing(number=i, win=False))
                    self.winsPlus+=1
        


    def MakeResult(self, draw: LottoDraw, bet: Bet):
        self.id=draw.id
        self.date=draw.date
        self.Compare(draw=draw.lotto, bet=bet.numbers, plus=bet.isplus)
        

class TypeChecker(ResultReport):

    results = [ResultReport]
    draws = [LottoDraw]

    def GetDrawsByPeriod (self, bet: Bet):
        start = bet.startdate
        end = bet.enddate
        self.draws=LottoDraw.objects.filter(date__range=(start, end))
    

    def MakeResults(self, bet: Bet):
        self.GetDrawsByPeriod(bet=bet)
        for draw in self.draws:
            result = ResultReport()
            result.MakeResult(draw=draw, bet=bet)
            self.results.append(result)
        



