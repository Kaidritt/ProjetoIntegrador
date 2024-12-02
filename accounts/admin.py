from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Residuo, PontoColeta

class ResiduoAdmin(admin.ModelAdmin):
    list_display = ('tipoResiduo', 'descricao', 'diretrizes')
    search_fields = ('tipoResiduo', 'descricao')

admin.site.register(Residuo, ResiduoAdmin)

class PontoColetaAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'latitude', 'longitude', 'tipo_residuo', 'horario')

    def tipo_residuo_link(self, obj):
        return format_html('<a href="{}">Adicionar outro</a>',
                           reverse('admin:app_tiporesiduo_add'))
    tipo_residuo_link.short_description = 'Adicionar Outro Tipo de Resíduo'

admin.site.register(PontoColeta, PontoColetaAdmin)