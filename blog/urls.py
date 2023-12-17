from django.urls import path
from . import views
urlpatterns = [
    # Paths del core

    path("", views.blog, name="blog"),
    #tomara los parametros que se toman en modificar blog para pasar la funcion de views llamada "category"
    #como los parentesis <> es considerado una cadena se tiene que declarar que es un entero
    path('category/<int:category_id>/',views.category,name="category")
]