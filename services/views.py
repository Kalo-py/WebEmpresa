from django.shortcuts import render
from .models import Service
#se crea una vista exclusiva para la carpeta services que seria una seccion aparte solo para services
def services(request):
    services = Service.objects.all()
    return render(request,"services/services.html", {'services':services})
