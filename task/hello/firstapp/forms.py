
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age")