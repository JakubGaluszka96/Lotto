from django import forms

class CreateNewType(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField()