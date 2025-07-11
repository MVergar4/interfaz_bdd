from django.db import models

class Paciente(models.Model):
    rut_paciente = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    tipo_sangre = models.CharField(max_length=3, blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    sistema_salud = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    calle = models.CharField(max_length=20, blank=True, null=True)
    numero_casa = models.CharField(max_length=10, blank=True, null=True)

class CalendarioDeCitas(models.Model):
    id_calendario = models.AutoField(primary_key=True)

class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    nombre = models.CharField(max_length=100)

class Odontologo(models.Model):
    rut_odontologo = models.CharField(max_length=10, primary_key=True)
    id_calendario = models.ForeignKey(CalendarioDeCitas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    numero_de_casa = models.CharField(max_length=10, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)

class FichaClinica(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    rut_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

class Medicamento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    dosis = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)

class Radiografia(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)

class EnfermedadBucal(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)

class RegistroDePago(models.Model):
    id_registro = models.AutoField(primary_key=True)
    boleta = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)
    rut_odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    id_registro = models.ForeignKey(RegistroDePago, on_delete=models.CASCADE)
    fecha = models.DateTimeField(blank=True, null=True)
    asunto = models.CharField(max_length=300, blank=True, null=True)
    bloque_horario = models.CharField(max_length=30, blank=True, null=True)

class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)
    rut_odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    id_registro = models.ForeignKey(RegistroDePago, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    presupuesto = models.IntegerField(blank=True, null=True)

class AccedeEdita(models.Model):
    id_ficha = models.ForeignKey(FichaClinica, on_delete=models.CASCADE)
    rut_odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_ficha', 'rut_odontologo'),)

class Usa(models.Model):
    rut_odontologo = models.ForeignKey(Odontologo, on_delete=models.CASCADE)
    id_material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        unique_together = (('rut_odontologo', 'id_material'),)
