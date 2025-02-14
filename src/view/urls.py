from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analysis/', views.analysis, name='analysis'),
    path('selection/', views.selection, name='selection'),
    path('about/', views.about, name='about'),
    path('topics/', views.topics, name='topics'),
    path('health/', views.health, name='health'),
    path('education/', views.education, name='education'),
    path('security/', views.security, name='security'),
    path('environment/', views.environment, name='environment'),
    path('culture/', views.culture, name='culture'),
    path('diversity/', views.diversity, name='diversity'),
    path('economy/', views.economy, name='economy'),
    path('housing/', views.housing, name='housing'),
    path('others/', views.others, name='others'),
    path('politics/', views.politics, name='politics'),
    path('technology/', views.technology, name='technology'),
    path('transportation/', views.transportation, name='transportation'),
    path('plotly_chart/<int:proposal_id>/', views.plotly_chart_view, name='plotly_chart_view'),
]

