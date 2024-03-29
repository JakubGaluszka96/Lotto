from django import forms
import numpy as np


class CheckType(forms.Form):
    INTEGER_CHOICES = [tuple([x,x]) for x in range(1,50)]
    number1 = forms.IntegerField(label="1 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number2 = forms.IntegerField(label="2 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number3 = forms.IntegerField(label="3 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number4 = forms.IntegerField(label="4 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number5 = forms.IntegerField(label="5 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number6 = forms.IntegerField(label="6 typ", widget=forms.Select(choices=INTEGER_CHOICES))
    startdate = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(1957, 2024),
    ),label="startdate",
)
    
    enddate = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),years=range(1957, 2024),
    ),label="enddate"
    )
    isplus= forms.BooleanField(label="isplus", required=False)

    def is_unique(self):
        numbers = [self.number1, self.number2, self.number3, self.number4, self.number5, self.number6]
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i !=j:
                    if numbers[i] == numbers[j]:
                        return False
        return True

class CreateNewBet(CheckType):
    name = forms.CharField(label="Name", max_length=200)

class Typing(forms.Form):
    INTEGER_CHOICES= [tuple()]
    number=forms.IntegerField(label="1", widget=forms.Select(choices=INTEGER_CHOICES))
    winner=forms.BooleanField(label="win", required=False)

    def __init__(self, maxNumber):
        INTEGER_CHOICES= [tuple([x,x]) for x in range(1,maxNumber)]
        return self
    def __init__(self):
        return self



            

