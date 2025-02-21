from django.contrib import admin
from django.utils.timezone import now
from django.shortcuts import redirect
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
from datetime import datetime
from .models import Comentario
from scripts.sentiment_analysys import start_batch_analysis, save_jsonl_files


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('body', 'sentiment', 'updated_at', 'analyzed_at')
    ordering = ('updated_at',)
    actions = ['executar_analise', 'finalizar_analise']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('analise-sentimentos/', self.admin_site.admin_view(self.analise_sentimentos),
                 name="analise_sentimentos"),
            path('finalizar-analise/', self.admin_site.admin_view(self.finalizar_analise), name="finalizar_analise"),
        ]
        return custom_urls + urls

    def executar_analise(self, request, queryset):
        return redirect('admin:analise_sentimentos')

    executar_analise.short_description = "Executar análise de sentimentos nos comentários"

    def analise_sentimentos(self, request):
        if request.method == "POST":
            data_inicio = request.POST.get("data_inicio", None)
            max_comentarios = int(request.POST.get("max_comentarios", 500))

            if data_inicio:
                data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
            else:
                data_inicio = None

            start_batch_analysis(since=data_inicio, max_comments=max_comentarios)

            self.message_user(request, "Análise de sentimentos concluída!")
            return redirect("..")  # Retorna para a página principal do Admin

        return TemplateResponse(request, "admin/analise_sentimentos.html", {})

    # Função para finalizar a análise de sentimentos
    def finalizar_analise(self, request, queryset):
        return redirect('admin:finalizar_analise')

    finalizar_analise.short_description = "Finalizar a análise de sentimentos"

    def finalizar_analise(self, request, queryset):
        # batch_job_id = request.session.get('batch_job_id')
        # file_name = request.session.get('file_name')
        # start_time = datetime.fromisoformat(request.session.get('start_time'))

        # if batch_job_id and file_name and start_time:
        #     client = OpenAI(api_key=os.getenv("LUMINA_OPENAI_API_KEY"))
        #     batch_job = client.batches.retrieve(batch_job_id)
        #     end_batch_analysis(batch_job, file_name, start_time)
        #     save_jsonl_files()

        #     self.message_user(request, "Análise de sentimentos finalizada e resultados salvos no banco de dados!")
        # else:
        #     self.message_user(request, "Erro ao finalizar a análise. Informações de sessão ausentes.", level='error')

        save_jsonl_files()

        self.message_user(request, "Análise de sentimentos salva no Banco de Dados!")

        return redirect("..")


admin.site.register(Comentario, ComentarioAdmin)
