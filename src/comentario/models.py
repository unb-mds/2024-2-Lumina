from django.db import models
from proposta.models import Proposta


class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    commentable_type = models.CharField(max_length=255)  #Decidim Commentable Type
    commentable_id = models.BigIntegerField(unique=True)  # ID
    author_id = models.BigIntegerField()  # Decidim Author ID
    body = models.CharField(max_length=10000)  # Body
    created_at = models.DateTimeField(null=True)  # Created At
    updated_at = models.DateTimeField()  #  Updated At
    proposta = models.ForeignKey(Proposta, related_name="comentarios",
                                 on_delete=models.CASCADE)  #conexão com as propostas
    analyzed_at = models.DateTimeField(default='2000-01-01 00:00:00.000000')  # ??
    sentiment = models.IntegerField(default=-1)  # análise de sentimentos

    def __str__(self):
        return self.body
