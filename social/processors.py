from .models import Link

def ctx_dict(request):
    ctx={}
    links=Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
    return ctx
# creamos una funcion que nos
# devuelva los modelos de link en general
# y se almacena en una variable diccionario, devolvera el valor de esta manera
# {key:url} esta funcion se usa para devolver las redes sociales almacenadas en el modelo de Link y devolverlo en el template de pie de pagina de base
