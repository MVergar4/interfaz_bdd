from django.shortcuts import render, HttpResponse
from .models import Cita

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def citas_view(request):
    citas = Cita.objects.select_related('id_ficha__rut_paciente').all()
    return render(request, 'citas.html', {'citas': citas})

def calendario_view(request):
    return render(request, 'calendario.html')

def inicio_view(request):
    return render(request, 'inicio.html')