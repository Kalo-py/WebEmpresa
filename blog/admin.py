from django.contrib import admin
from .models import Category,Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    #como sabras esta seccion es donde podemos visualizar los datos de los proyectos
    #desde el admin y podemos añadir que se vea tambien los campos de autor y titulo
    #con solamente readonly se ve el titulo del proyecto pero con list_display nos mostrara mas datos
    #ejemplo el autor, titulo, y fecha publicada, etos campos de title,author etc son variables invocados
    #desde el models de blog en la funcion "POST"
    list_display = ('title','author','published','post_categories')
    #Estás indicando que los objetos del modelo se deben ordenar primero por el campo
    #author y luego por el campo published en caso de que haya autores con el
    #mismo nombre.
    ordering = ('author','published')
    #se utiliza en las clases de administración para
    #especificar los campos por los cuales se puede realizar una búsqueda
    # en la interfaz de
    #administración.
    #es decir crea un buscador para los titulos de tu modelo
    #y como es una tupla, despues de title debe venir una coma o sino arrojara un error
    search_fields = ('title','content','author__username','categories__name') #obs para buscar un autor no se puede poner
    # solamente la variable author, se debe poner con el usuario en este caso username
    #tambien para categorias

    date_hierarchy = 'published' #permite ver por fechas de los proyectos

    list_filter = ('author__username','categories__name')

    #metodo para mostrar que tipo de categoria es el proyecto
    def post_categories(self,obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
        #saca el nombre de las categorias ordenadamente por nombres con un ciclo for
    post_categories.short_description = "Categorias" #permite cambiar el nombre de la
    # funcion post_categories para que devuelva otro nombre distinto en el listado
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)