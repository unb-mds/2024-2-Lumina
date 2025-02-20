from django.shortcuts import render
from scripts.get_df import get_proposal_dic, get_proposal_df
from proposta.models import Proposta
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objs as go
from django.urls import path
from django.db.utils import OperationalError


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
    try:
        propostas = Proposta.objects.filter(topic='Saúde').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'health.html', {'propostas': propostas})


def education(request):
    try:
        propostas = Proposta.objects.filter(topic='Educação').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'education.html', {'propostas': propostas})


def security(request):
    try:
        propostas = Proposta.objects.filter(topic='Segurança').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'security.html', {'propostas': propostas})


def environment(request):
    try:
        propostas = Proposta.objects.filter(topic='Meio Ambiente').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'environment.html', {'propostas': propostas})


def culture(request):
    try:
        propostas = Proposta.objects.filter(topic='Cultura').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'culture.html', {'propostas': propostas})


def diversity(request):
    try:
        propostas = Proposta.objects.filter(topic='Diversidade').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'diversity.html', {'propostas': propostas})


def economy(request):
    try:
        propostas = Proposta.objects.filter(topic='Economia').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'economy.html', {'propostas': propostas})


def housing(request):
    try:
        propostas = Proposta.objects.filter(topic='Habitação').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'housing.html', {'propostas': propostas})


def others(request):
    try:
        propostas = Proposta.objects.filter(topic='Outros').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'others.html', {'propostas': propostas})


def politics(request):
    try:
        propostas = Proposta.objects.filter(topic='Politica').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'politics.html', {'propostas': propostas})


def technology(request):
    try:
        propostas = Proposta.objects.filter(topic='Tecnologia').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'technology.html', {'propostas': propostas})


def transportation(request):
    try:
        propostas = Proposta.objects.filter(topic='Transporte').order_by('-comments_count')
        if not propostas.exists():
            raise Proposta.DoesNotExist
    except (OperationalError, Proposta.DoesNotExist):
        error_message = "Erro: Não há propostas disponíveis ou as migrações não foram realizadas."
        return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'transportation.html', {'propostas': propostas})


def plotly_chart_view(request, proposal_id):
    data = get_proposal_dic(proposal_id)
    df = get_proposal_df(proposal_id)
    proposal = Proposta.objects.get(id=proposal_id)
    proposal_name = proposal.title
    comments = proposal.comentarios.all()  # Corrigir o acesso aos comentários

    fig = px.pie(df, values='Comentários', names='Opinião', title=proposal_name)
    plot_div = plot(fig, output_type='div')

    return render(request, 'plotly_chart.html', {'plot_div': plot_div, 'comments': comments})
