
from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class': 'myfield'}))
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={'class': 'myfield'}))