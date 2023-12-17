from django.shortcuts import render, get_object_or_404 #este sirve para los errores de pagina que no existen
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {'posts':posts})

def category(request, category_id):
    # Obtiene la categoría específica utilizando el ID proporcionado en la URL
    #utilizamos el get 404 para que pueda mostrar en caso de que se toma mal un id
    category= get_object_or_404(Category,id=category_id)
    posts= Post.objects.filter(categories=category)
    # Renderiza la plantilla "blog/category.html" y pasa la categoría como contexto
    return render(request,"blog/category.html",{'category':category,
                                                    'posts':posts})
    # En resumen, la línea de código en cuestión se encarga de recuperar
    # todas las publicaciones que están asociadas a una categoría específica,
    # utilizando la relación establecida en el modelo Post.