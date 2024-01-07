from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    #list_display nos permite ver en el admin estos campos y podemos ver en orden de acuerdo al titulo u orden que estan los modelos
    list_display = ('title','order')

admin.site.register(Page,PageAdmin)