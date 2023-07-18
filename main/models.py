from django.db import models
from django.contrib.auth.models import User
from .forms import CheckType

# Create your models here.

class BetList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

      
class Bet(models.Model):
    id = models.IntegerField(primary_key=True)
    typeslist = models.ForeignKey(BetList, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    is_plus = models.BooleanField()

    def parse_form(self, form: CheckType):
        self.startdate=form.cleaned_data["startdate"]
        self.enddate=form.cleaned_data["enddate"]
        self.is_plus=form.cleaned_data["isplus"]
        numbers = [form.cleaned_data["number1"], 
                   form.cleaned_data["number2"], 
                   form.cleaned_data["number3"], 
                   form.cleaned_data["number4"], 
                   form.cleaned_data["number5"], 
                   form.cleaned_data["number6"]]
        for i in numbers:           
            self.number_set.create(number=i)

    def get_numbers(self):
        numbers = []
        for number in self.number_set.all():
                numbers.append(number)
        return numbers




    
class Number(models.Model):
    bet = models.ForeignKey(Bet, on_delete=models.CASCADE)
    number = models.IntegerField()
    win = models.BooleanField()



class LottoDraw(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()

    def get_typing_list(self):
        lotto = []
        for i in self.typing_set.all():
                lotto.append(i)
        return lotto


class Typing(models.Model):
    draw = models.ForeignKey(LottoDraw, on_delete=models.CASCADE, db_constraint=False)
    number = models.IntegerField()
    is_plus = models.BooleanField()

    def __str__(self):
        return self    


