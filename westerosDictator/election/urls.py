from unicodedata import name
from django.urls import path
from . import views

app_name = 'election'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:election_id>/', views.detail, name='detail'),
    path('<int:election_id>/resultats/', views.resultats, name='resultats'),
    path('<int:election_id>/liste/', views.liste, name='liste'),
    path('<int:election_id>/vote/', views.vote, name='vote'),
]