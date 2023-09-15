from django import forms

TEMP_CHOICES = [
    ('Celcius', 'Celcius'),
    ('Kelvin', 'Kelvin'),
    ('Fahrenheit', 'Fahrenheit')
]
class tempForm(forms.Form):
    from_unit = forms.ChoiceField(choices=TEMP_CHOICES, label='Dari')
    to_unit = forms.ChoiceField(choices=TEMP_CHOICES, label='Ke')
    temperature = forms.FloatField(label='Temperatur')
