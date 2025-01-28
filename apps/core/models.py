from django.db import models

class Proposta(models.Model):
    component_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    votes_count = models.IntegerField(default=0)
    title = models.CharField(max_length=300)
    title_lang = models.CharField(max_length=25)
    body = models.CharField(max_length=10000)
    body_lang = models.CharField(max_length=25)
    comments_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comentario(models.Model):
    commentable_id = models.BigIntegerField(primary_key=True)
    author_id = models.BigIntegerField()
    body = models.CharField(max_length=10000)
    body_lang = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()
    proposta = models.ForeignKey(Proposta, related_name="comentarios", on_delete=models.CASCADE)
    root_comment_id = models.BigIntegerField()
    analyzed_at = models.DateTimeField()
    sentiment = models.IntegerField(default=-1)
    prompt_version = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.body
