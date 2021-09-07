from django.urls import path

from . import views

app_name = 'encuestas'
urlpatterns = [
    # ex: /encuestas/
    path('', views.index, name='index'),
    # ex: /encuestas/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /encuestas/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /encuestas/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]