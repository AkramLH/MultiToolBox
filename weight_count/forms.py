from django import forms

class weightForm(forms.Form):
    age = forms.IntegerField(label='age')
    weight = forms.FloatField(label='weight (kg)')
    height = forms.FloatField(label='height (cm)')
