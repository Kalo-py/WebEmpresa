from django.urls import path
from . import views
#se crea una direccion para la carpeta services que seria una seccion aparte solo para services
urlpatterns = [
    # Paths del core
    path("", views.services, name="services")
]