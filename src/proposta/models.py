from django.db import models

class Proposta(models.Model):
    id = models.BigAutoField(primary_key=True)
    component_id = models.IntegerField(unique=True) #ID
    created_at = models.DateTimeField(default='2000-01-01 00:00:00.000000') #Created At
    updated_at = models.DateTimeField(default='2000-01-01 00:00:00.000000') #Updated At
    votes_count = models.IntegerField(default=0) #Proposal Votes Count
    title = models.CharField(max_length=1000, default='Proposal not found') #Title
    body = models.CharField(max_length=50000, default='Proposal not found') #Body
    comments_count = models.IntegerField(default=0) #Comments Count
    topic = models.CharField(max_length=1000, default='Proposal not found') #Topic of the proposal

    def __str__(self):
        return self.title.get("pt-BR", "Título não definido")
