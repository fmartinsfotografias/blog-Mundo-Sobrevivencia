from csv import list_dialects
from django.contrib import admin
from .models import Materia


class ListandoMaterias(admin.ModelAdmin):
    list_display = ('id', 'nome_materia', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_materia', )
    search_fields = ('nome_materia', )
    list_filter = ('categoria', )
    list_editable = ('publicada',)
    list_per_page = 10


# Register your models here.

admin.site.register(Materia, ListandoMaterias)
