from django.contrib import admin
from django.utils.timezone import now
from django.shortcuts import redirect
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
from datetime import datetime
from .models import Comentario
from scripts.sentiment_analysys import serial_analysis, batch_analysis 

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('body', 'sentiment', 'updated_at', 'analyzed_at')
    ordering = ('updated_at',)
    actions = ['executar_analise']

    def executar_analise(self, request, queryset):
        return redirect('admin:analise_sentimentos')

    executar_analise.short_description = "Executar análise de sentimentos nos comentários"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('analise-sentimentos/', self.admin_site.admin_view(self.analise_sentimentos), name="analise_sentimentos"),
        ]
        return custom_urls + urls

    def analise_sentimentos(self, request):
        if request.method == "POST":
            data_inicio = request.POST.get("data_inicio", None)
            max_comentarios = int(request.POST.get("max_comentarios", 500))
            
            if data_inicio:
                data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
            else:
                data_inicio = None
            
            batch_analysis(since=data_inicio, max_comments=max_comentarios)

            self.message_user(request, "Análise de sentimentos concluída!")
            return redirect("..")  # Retorna para a página principal do Admin

        return TemplateResponse(request, "admin/analise_sentimentos.html", {})

admin.site.register(Comentario, ComentarioAdmin)
