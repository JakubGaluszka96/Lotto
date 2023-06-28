from django.db import models

# Create your models here.

class BetList(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
      
class Bet(models.Model):
    id = models.IntegerField(primary_key=True)
    typeslist = models.ForeignKey(BetList, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    isplus = models.BooleanField()

    def assign(self, form):
        self.startdate=form.cleaned_data["startdate"]
        self.enddate=form.cleaned_data["enddate"]
        self.isplus=form.cleaned_data["isplus"]


    
class LottoDraws(models.Model):


    pass

class LottoDraw(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()


class Typing(models.Model):
    betlist = models.ForeignKey(LottoDraw, on_delete=models.CASCADE, db_constraint=False)
    number = models.IntegerField()
    isplus = models.BooleanField()

    def __str__(self):
        return self    


