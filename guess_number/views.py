from django.shortcuts import render

def guessNumber(request):
    
    return render(request, 'guess_number.html')