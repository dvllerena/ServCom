from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'miapp/home.html')

def index(request):
    return render(request, 'miapp/index.html')

def proyectos(request):
    return render(request, 'miapp/proyectos.html')

def contacto(request):
    return render(request, 'miapp/contacto.html')

@login_required
def dashboard(request):
    return render(request, 'miapp/dashboard.html')

def registro(request):
    return render(request, 'miapp/registro.html')
