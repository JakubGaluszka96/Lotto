from django.db import models
from django.contrib.auth.models import User
from .forms import CheckType

# Create your models here.    

      
class UserBet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userbet", null=True)
    name = models.CharField(max_length=1000, null=False)
    startdate = models.DateField()
    enddate = models.DateField()
    is_plus = models.BooleanField()

    def get_numbers(self):
        numbers = []
        for number in self.number_set.all():
                numbers.append(number.number)
        return numbers

 
class Number(models.Model):
    userbet = models.ForeignKey(UserBet, on_delete=models.CASCADE, db_constraint=False, null=True, blank=True)
    number = models.IntegerField()
    win = models.BooleanField()    
    
    def __str__(self):
        return self  


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


