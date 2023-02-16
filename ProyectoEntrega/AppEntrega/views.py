from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def inicio(request):
    return render(request,"AppEntrega/inicio.html")

def estilo(request):
    return render(request,"AppEntrega/estilo.html")

def truco (request):
    return render(request,"AppEntrega/truco.html")

def mago (request):
    return render(request,"AppEntrega/mago.html")