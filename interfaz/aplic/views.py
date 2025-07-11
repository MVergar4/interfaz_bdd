from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def citas_view(request):
    return render(request, 'citas.html')

def calendario_view(request):
    return render(request, 'calendario.html')