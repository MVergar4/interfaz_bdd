from django.contrib import admin

from .models import (
    Paciente,
    Material,
    CalendarioDeCitas,
    Odontologo,
    FichaClinica,
    Medicamento,
    Radiografia,
    EnfermedadBucal,
    RegistroDePago,
    Cita,
    Tratamiento,
    AccedeEdita,
    Usa,
)

admin.site.register(Paciente)
admin.site.register(Material)
admin.site.register(CalendarioDeCitas)
admin.site.register(Odontologo)
admin.site.register(FichaClinica)
admin.site.register(Medicamento)
admin.site.register(Radiografia)
admin.site.register(EnfermedadBucal)
admin.site.register(RegistroDePago)
admin.site.register(Cita)
admin.site.register(Tratamiento)
admin.site.register(AccedeEdita)
admin.site.register(Usa)
