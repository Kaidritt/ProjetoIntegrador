from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Residuo, PontoColeta

class ResiduoAdmin(admin.ModelAdmin):
    list_display = ('tipoResiduo', 'descricao', 'diretrizes')
    search_fields = ('tipoResiduo', 'descricao')

admin.site.register(Residuo, ResiduoAdmin)

class PontoColetaAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'latitude', 'longitude')
    search_fields = ('endereco',)
    filter_horizontal = ('tipos_residuo',)

admin.site.register(PontoColeta, PontoColetaAdmin)