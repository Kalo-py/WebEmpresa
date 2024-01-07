from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title=models.CharField(verbose_name="Titulo",max_length=200)
    #con ckeditor importado nos permite modificar el contenido del texto como si fuese un word
    content=RichTextField(verbose_name="Contenido")
    #order seria el formato valor numerico que tendrian los elementos del modelo
    order=models.SmallIntegerField(verbose_name="Orden",default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name="página"
        verbose_name_plural="páginas"
        ordering=['order','title']

    def __str__(self):
        return self.title