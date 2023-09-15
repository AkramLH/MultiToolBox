from django.shortcuts import render
from .forms import tempForm

def tempConvert(request):
    result = None
    
    if request.method == 'POST':
        form = tempForm(request.POST)
        if form.is_valid():
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            temperature = form.cleaned_data['temperature']
            
            if from_unit == 'Celcius' and to_unit == 'Fahrenheit':
                result = round((temperature * 9/5) + 32,3)
            elif from_unit == 'Celcius' and to_unit == 'Kelvin':
                result = round(temperature + 273.15,3)
            elif from_unit == 'Kelvin' and to_unit == 'Celcius':
                result = round(temperature - 273.15,3)
            elif from_unit == 'Fahrenheit' and to_unit == 'Celcius':
                result = round((5/9) * (temperature - 32),3)
            elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
                result = round((9/5) * (temperature - 273.15) + 32,3)
            elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
                result = round((5/9) * (temperature - 32) + 273.15,3)
    else:
        form = tempForm() 
    
    context = {
        'form': form,
        'result': result,
    }
    
    return render(request, 'temp_convert.html', context)
