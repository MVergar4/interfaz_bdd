from django.urls import path
from . import views
from .views import citas_view, calendario_view

urlpatterns = [
    path("", views.home, name="home"),
    path('citas/', citas_view, name='citas'),
    path('calendario/', calendario_view, name='calendario')
]
