from django.contrib import admin
from .models import Proposta

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')

admin.site.register(Proposta)