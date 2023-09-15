from django.shortcuts import render
from .forms import weightForm

def weightCount(request):
    bmi = 0
    weight_category = ''

    if request.method == 'POST':
        # Inisialisasi formulir dengan data yang dikirimkan oleh pengguna
        form = weightForm(request.POST)
        if form.is_valid():
            # Mendapatkan data yang telah divalidasi dari formulir
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            age = form.cleaned_data['age']

            height_m = height / 100  # Konversi tinggi dari cm ke meter
            bmi = weight / (height_m ** 2)
            # Format BMI menjadi satu angka di belakang koma
            bmi = round(bmi, 1)

            if age < 18:
                # weight_category = 'Kategori Usia Dibawah 18 Tahun'
                # Kategori BMI percentile berdasarkan usia dan persentase berat badan terhadap tinggi badan
                if age <= 2:
                    if bmi < 5:
                        weight_category = 'Underweight (<5%)'
                    elif 5 <= bmi <= 85:
                        weight_category = 'Healthy weight (5% - 85%)'
                    elif 85 < bmi <= 95:
                        weight_category = 'At risk of overweight (85% - 95%)'
                    else:
                        weight_category = 'Overweight (>95%)'
                elif 2 < age <= 18:
                    if bmi < 5:
                        weight_category = 'Underweight (<5%)'
                    elif 5 <= bmi <= 85:
                        weight_category = 'Healthy weight (5% - 85%)'
                    elif 85 < bmi <= 95:
                        weight_category = 'At risk of overweight (85% - 95%)'
                    else:
                        weight_category = 'Overweight (>95%)'
            else:
                if bmi < 18.5:
                    weight_category = 'Underweight (Kekurangan Berat Badan)'
                elif 18.5 <= bmi < 24.9:
                    weight_category = 'Normal'
                elif 25 <= bmi < 29.9:
                    weight_category = 'Overweight (Kelebihan Berat Badan)'
                else:
                    weight_category = 'Obesity (Obesitas)'
    else:
        form = weightForm()  # Inisialisasi formulir hanya pada GET request

    context = {
        'form': form,
        'bmi': bmi,
        'weight_category': weight_category,
    }
    return render(request, 'weight_count.html', context)
