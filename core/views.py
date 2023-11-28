from django.shortcuts import render, HttpResponse

# Create your views here.
"""
Inicio home/
Historia about/
Servicios services/
Visitanos store/
Contacto contact/
Blog blog/
Sample sample/
"""

def home(request):
    return httpResponse("Inicio")

def about(request):
    return httpResponse("Historia")

def services(request):
    return httpResponse("Servicios")

def store(request):
    return httpResponse("Visitanos")

def contact(request):
    return httpResponse("Contacto")

def blog(request):
    return httpResponse("Blog")

def sample(request):
    return httpResponse("Sample")