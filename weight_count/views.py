from django.shortcuts import render

def weightCount(request):
    bmi = 0
    weight_category = ''

    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        age = int(request.POST['age'])

        height_m = height / 100  # Konversi tinggi dari cm ke meter
        bmi = weight / (height_m ** 2)

        if age < 18:
            weight_category = 'Kategori Usia Dibawah 18 Tahun'
        else:
            if bmi < 18.5:
                weight_category = 'Underweight (Kekurangan Berat Badan)'
            elif 18.5 <= bmi < 24.9:
                weight_category = 'Normal'
            elif 25 <= bmi < 29.9:
                weight_category = 'Overweight (Kelebihan Berat Badan)'
            else:
                weight_category = 'Obesity (Obesitas)'

        context = {
            'bmi': bmi,
            'weight_category': weight_category,
        }
        return render(request, 'weight_count.html', context)
    else:
        return render(request, 'weight_count.html')
