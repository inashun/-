from django.shortcuts import render
from django.http import HttpResponse
from .forms import CalcPlusForm

def index(request):
    params = {
        'title':'CalcPlus',
        'forms': CalcPlusForm(),
        'answer':'Answer is '
    }
    if (request.method == 'POST'):
        params['answer'] = 'Answer is ' + str(int(request.POST['val1']) + int(request.POST['val2'])) 
        params['forms'] = CalcPlusForm(request.POST)
    return render(request, 'calcplus/index.html', params)