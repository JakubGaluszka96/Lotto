from django import forms

maxNumber=50
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,maxNumber)]

class CreateNewType(forms.Form):
    name = forms.CharField(label="Name", max_length=200)

class CheckType(forms.Form):
    
    number1 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number2 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number3 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number4 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number5 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    number6 = forms.IntegerField(label="Pierwszy typ", widget=forms.Select(choices=INTEGER_CHOICES))
    startdate = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)
    enddate = forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
    )

    isplus= forms.BooleanField(label="isplus", required=False)



