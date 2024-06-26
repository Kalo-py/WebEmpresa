"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #Paths del core
    #el include permite traer el contenido del archivo urls.py
    # que esta en urls dentro de la carpeta core
    path('', include('core.urls')),

    #Paths del services
    path('services/', include('services.urls')),
    #Paths del services
    path('blog/', include('blog.urls')),
    #Paths del pages
    path('page/', include('pages.urls')),
    #Paths del contact
    path('contact/', include('contact.urls')),
    # Paths del admin
    path("admin/", admin.site.urls),
]

#permite corroborar si el debug esta en marcha
#esto permite crear una url para los archivos en /media/ en setting
#y se alojaran en el directorio de carpetas media que esta definido
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#Custom titles for admin
admin.site.site_header="La cafeteria"
admin.site.index_title="Panel de administrador"
admin.site.site_title = "La cafetera"