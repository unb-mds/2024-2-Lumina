from django.shortcuts import render
from scripts.get_df import get_proposal_df
from proposta.models import Proposta
import plotly.express as px
from django.urls import path

def index(request):
    return render(request, 'home.html')

def analysis(request):
    return render(request, "analysis.html")
    
def selection(request):
    return render(request, "selection_page_feelings.html")
    
def about(request):
    return render(request, 'aboutus.html')

def topics(request):
    return render(request, 'selection_topics.html')



def health(request):
    propostas = Proposta.objects.filter(topic='Saúde').order_by('-comments_count')
    return render(request, 'health.html', {'propostas': propostas})
    
def education(request):
    propostas = Proposta.objects.filter(topic='Educação').order_by('-comments_count')
    return render(request, 'education.html', {'propostas': propostas})
    
def security(request):
    propostas = Proposta.objects.filter(topic='Segurança').order_by('-comments_count')
    return render(request, 'security.html', {'propostas': propostas})
    
def environment(request):
    propostas = Proposta.objects.filter(topic='Meio Ambiente').order_by('-comments_count')
    return render(request, 'environment.html', {'propostas': propostas})

def culture(request):
    propostas = Proposta.objects.filter(topic='Cultura').order_by('-comments_count')
    return render(request, 'culture.html', {'propostas': propostas})

def diversity(request):
    propostas = Proposta.objects.filter(topic='Diversidade').order_by('-comments_count')
    return render(request, 'diversity.html', {'propostas': propostas})

def economy(request):
    propostas = Proposta.objects.filter(topic='Economia').order_by('-comments_count')
    return render(request, 'economy.html' , {'propostas': propostas})

def housing(request):
    propostas = Proposta.objects.filter(topic='Habitação').order_by('-comments_count')
    return render(request, 'housing.html', {'propostas': propostas})

def others(request):
    propostas = Proposta.objects.filter(topic='Outros').order_by('-comments_count')
    return render(request, 'others.html', {'propostas': propostas})

def politics(request):
    propostas = Proposta.objects.filter(topic='Politica').order_by('-comments_count')
    return render(request, 'politics.html', {'propostas': propostas})

def technology(request):
    propostas = Proposta.objects.filter(topic='Tecnologia').order_by('-comments_count')
    return render(request, 'technology.html', {'propostas': propostas})

def transportation(request):
    propostas = Proposta.objects.filter(topic='Transporte').order_by('-comments_count')
    return render(request, 'transportation.html', {'propostas': propostas})


def plotly_chart_view(request, proposal_id):
    df = get_proposal_df(proposal_id)
    proposal_name = Proposta.objects.get(id=proposal_id).title

    # fig = px.pie(df, values='Comentários', names='Opinião', title=proposal_name)
    fig = px.bar(df, x='Comentários', y='Opinião', title=proposal_name, orientation='h')
    plotly_chart = fig.to_json()

    return render(request, 'plotly_chart.html', {'plotly_chart': plotly_chart})
