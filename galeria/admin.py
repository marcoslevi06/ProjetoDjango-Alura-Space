from django.contrib import admin

from galeria.models import *

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'foto')
    list_display_links = ('id', 'nome', 'legenda')
    search_fields = ('nome', 'legenda', 'descricao')
    list_filter = ('nome', 'legenda', 'foto')

admin.site.register(Fotografia, FotografiaAdmin)