from django.shortcuts import render, HttpResponse
from .models import Cita
import re
from datetime import datetime, timedelta, date

DIAS_SEMANA = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']

# Create your views here.
def home(request):
    return HttpResponse("Hello World")

def citas_view(request):
    citas = Cita.objects.select_related('id_ficha__rut_paciente').all()
    return render(request, 'citas.html', {'citas': citas})

def inicio_view(request):
    return render(request, 'inicio.html')

def get_all_weeks_of_year(year):
    # Encontrar el primer lunes del año
    first_day = date(year, 1, 1)
    days_to_monday = (7 - first_day.weekday()) % 7
    first_monday = first_day if first_day.weekday() == 0 else first_day + timedelta(days=days_to_monday)

    weeks = []
    current = first_monday
    while current.year == year or (current.year == year + 1 and current.month == 1):
        weeks.append(current.strftime("%Y-%m-%d"))
        current += timedelta(weeks=1)
    return weeks

def extraer_hora_fecha(bloque):
    if not bloque:
        return None, None
    try:
        partes = bloque.split('_')
        hora_parte = partes[0].strip('[]').strip()
        fecha_parte = partes[1].strip('[]').strip().replace('/', '-')

        # Extraer todas las horas válidas
        horas_encontradas = re.findall(r'\d{1,2}:\d{2}', hora_parte)
        if horas_encontradas:
            hora_inicio = horas_encontradas[0]
        else:
            hora_inicio = hora_parte

        return hora_inicio, fecha_parte
    except (IndexError, AttributeError):
        return None, None

def get_week_start(date):
    # Ajusta para que lunes sea el inicio de la semana
    return date - timedelta(days=date.weekday())

def calendario_view(request):

    # Obtener la semana seleccionada desde GET
    semana_param = request.GET.get('semana')
    if semana_param:
        try:
            semana_inicio = datetime.strptime(semana_param, "%Y-%m-%d").date()
        except ValueError:
            semana_inicio = get_week_start(datetime.today().date())
    else:
        semana_inicio = get_week_start(datetime.today().date())

    semana_fin = semana_inicio + timedelta(days=6)
    print("Semana seleccionada:", semana_inicio, "-", semana_fin)

    citas_raw = Cita.objects.select_related('id_ficha__rut_paciente').all()

    citas_por_key = {}

    for cita in citas_raw:
        hora_str, fecha_str = extraer_hora_fecha(cita.bloque_horario)
        print("Cita:", cita.id_cita, "bloque_horario:", cita.bloque_horario, "=> hora:", hora_str, "fecha:", fecha_str)
        if hora_str and fecha_str:
            try:
                fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                if semana_inicio <= fecha_dt <= semana_fin:
                    dia_en = fecha_dt.strftime("%A")
                    traduccion = {
                        "Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miercoles",
                        "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sabado",
                        "Sunday": "Domingo"
                    }
                    dia_es = traduccion.get(dia_en, dia_en)
                    key = f"{hora_str.strip().lower()}-{dia_es.strip().lower()}"
                    print("✅ Aceptada:", fecha_dt, "es", dia_es, "en clave:", key)

                    citas_por_key.setdefault(key, []).append({
                        'nombre': cita.id_ficha.rut_paciente.nombre,
                        'rut': cita.id_ficha.rut_paciente.rut_paciente
                    })
            except ValueError:
                pass

    # Generar horarios
    horarios = []
    hora_actual = 9
    minuto_actual = 0
    while hora_actual < 20:
        horario = f"{hora_actual:02d}:{minuto_actual:02d}"
        horarios.append(horario)
        minuto_actual += 30
        if minuto_actual == 60:
            minuto_actual = 0
            hora_actual += 1

    # Generar lista de semanas disponibles (últimas 4 semanas + actual)
    year_actual = datetime.today().year
    semanas_disponibles = get_all_weeks_of_year(year_actual)
    for i in range(0, 5):
        start = get_week_start(datetime.today().date() - timedelta(weeks=i))
        semanas_disponibles.append(start.strftime("%Y-%m-%d"))

    context = {
        'dias_semana': DIAS_SEMANA,
        'horarios': horarios,
        'citas': citas_por_key,
        'semana_actual': semana_inicio.strftime("%Y-%m-%d"),
        'semanas_disponibles': semanas_disponibles,
    }
    return render(request, 'calendario.html', context)