from django.shortcuts import render

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
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def services(request):
    return render(request,"core/services.html")

def store(request):
    return render(request,"core/store.html")

def contact(request):
    return render(request,"core/contact.html")

def blog(request):
    return render(request,"core/bloghome.html")

def sample(request):
    return render(request,"core/sample.html")