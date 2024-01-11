from django.shortcuts import render
from django.http import HttpResponse
from .forms import BMIForm

def index(request):
    params = {
        'title':'BMI APP',
        'forms':BMIForm(),
    }
    if (request.method == 'POST'):
        height = int(request.POST['height'])
        weight = int(request.POST['weight'])

        params['forms'] = BMIForm(request.POST)

        bmi = round(weight / ((height/100) * (height/100)), 1)
        optimal = round((height/100) * (height/100) * 22, 1)

        difference = round(abs(weight - optimal), 1)
        if bmi < 18.5:
            result = f'「痩せ」です。標準体重まで{difference}kgです。'
        elif 18.5 <= bmi < 25:
            result = f'「普通体重」です。'
        elif 25 <= bmi < 30:
            result = f'「肥満（1度）」です。標準体重より{difference}kg多いです。'
        elif 30 <= bmi < 35:
            result = f'「肥満（2度）」です。標準体重より{difference}kg多いです。'
        elif 35 <= bmi < 40:
            result = f'「肥満（3度）」です。標準体重より{difference}kg多いです。'
        elif 40 <= bmi:
            result = f'「肥満（4度）」です。標準体重より{difference}kg多いです。'

        params['bmi'] = bmi
        params['optimal'] = optimal
        params['result'] = result

    return render(request, 'bmiapp/index.html', params)