from django.urls import path
from . import views
from .views import citas_view, calendario_view

urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('citas/', views.citas_view, name='citas'),
    path('calendario/', views.calendario_view, name='calendario')

]
