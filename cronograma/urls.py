from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.cronograma_index, name='cronograma_index'),
    path('gerente/cronogramas/', views.listado_cronogramas, name='listado_cronogramas')
]
