from django.shortcuts import redirect, render, HttpResponse
from .models import Cotacao
import random

def index(request):
    cot=Cotacao.objects.all()
    return render(request, 'index.html', {'cot': cot})

def form(request):
    return render(request, 'form.html')
 


def formrec(request):
    x=request.POST['First']
    y=request.POST['First']
    z=request.POST['First']
    cot=Cotacao(cnpjOne=x, nomeEmprOne=y, endOne=z)
    cot.save()
    return redirect('/')

def delete(request, id):
    cot=Cotacao.objects.get(id=id)
    cot.delete()
    return redirect('/')

def update(request, id):
    cot=Cotacao.objects.get(id=id)
    return render(request, 'update.html', {'cot':cot})

def uprec(request, id):
    x=request.POST['First']
    y=request.POST['last']
    z=request.POST['country']
    cot=Cotacao.objects.get(id=id)
    cot.cnpjOne=x
    cot.last=y
    cot.country=z
    cot.save()
    return redirect('/')

def cota(request):
    rand = random.randint(0, 1000000)
    return render(request, 'cota.html', {'rand':rand})

def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    num3 = int(request.GET['num3'])
    num4 = int(request.GET['num4'])
    num5 = int(request.GET['num5'])
    num6 = int(request.GET['num6'])
    calc1 = num6 / 100 * 0.4
    res = calc1 + num1 * num2 * num4 * num5 * 300 * 0.33

    return render(request, 'result.html', {'result': res})