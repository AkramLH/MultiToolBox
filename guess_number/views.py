from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from random import randint

no_rahasia = randint(0, 100)
kali = 0
berhasil = False

@csrf_exempt
def guessNumber(request):
    
    global no_rahasia, kali, berhasil
    context = {}
    hint = ''
    no_tertebak = None

    if request.method == 'POST' and request.POST.get('tebakan'):
        no_tertebak = int(request.POST['tebakan'])
        kali +=1
        if no_tertebak == no_rahasia:
            berhasil = True
        else:
            if(no_tertebak > no_rahasia):
                hint = 'terlalu tinggi'
            else:
                hint = 'terlalu rendah'
        
    else:
        no_rahasia = randint(0,100)
        kali = 0
        berhasil = False
        hint = ''
        no_tertebak = None
    
    context['berhasil'] = berhasil
    context['kali'] = kali
    context['hint'] = hint
    context['no_tertebak'] = no_tertebak

    return render(request, 'guess_number.html', context)

