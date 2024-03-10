from django.contrib import admin
from .models import Cotacao

class CotacaoAdmin(admin.ModelAdmin):
    list_display='cnpjOne','nomeEmprOne','endOne','cnpjTwo', 'nomeEmprTwo','endTwo','valorNf','pesoNf','quantNf','valorCota'

admin.site.register(Cotacao,CotacaoAdmin)