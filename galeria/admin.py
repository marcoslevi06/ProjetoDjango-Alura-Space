from django.contrib import admin

from galeria.models import *

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada', 'data_criacao')
    list_display_links = ('id', 'nome', 'legenda',)
    search_fields = ('nome', 'legenda', 'descricao')
    list_filter = ('nome', 'legenda',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Fotografia, FotografiaAdmin)