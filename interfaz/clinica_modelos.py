# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccedeEdita(models.Model):
    pk = models.CompositePrimaryKey('id_ficha', 'rut_odontologo')
    id_ficha = models.ForeignKey('FichaClinica', models.DO_NOTHING, db_column='id_ficha')
    rut_odontologo = models.ForeignKey('Odontologo', models.DO_NOTHING, db_column='rut_odontologo')

    class Meta:
        managed = False
        db_table = 'accede_edita'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calendariodecitas(models.Model):
    id_calendario = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'calendariodecitas'


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey('FichaClinica', models.DO_NOTHING, db_column='id_ficha')
    rut_odontologo = models.ForeignKey('Odontologo', models.DO_NOTHING, db_column='rut_odontologo', blank=True, null=True)
    id_registro = models.ForeignKey('RegistroDePago', models.DO_NOTHING, db_column='id_registro')
    fecha = models.DateTimeField(blank=True, null=True)
    asunto = models.CharField(max_length=300, blank=True, null=True)
    bloque_horario = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cita'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnfermedadBucal(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey('FichaClinica', models.DO_NOTHING, db_column='id_ficha')

    class Meta:
        managed = False
        db_table = 'enfermedad_bucal'


class FichaClinica(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    rut_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='rut_paciente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_clinica'


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'material'


class Medicamento(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    dosis = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey(FichaClinica, models.DO_NOTHING, db_column='id_ficha')

    class Meta:
        managed = False
        db_table = 'medicamento'


class Odontologo(models.Model):
    rut_odontologo = models.CharField(primary_key=True, max_length=10)
    id_calendario = models.ForeignKey(Calendariodecitas, models.DO_NOTHING, db_column='id_calendario')
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField(blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    ciudad = models.CharField(max_length=50, blank=True, null=True)
    numero_de_casa = models.CharField(max_length=10, blank=True, null=True)
    calle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'odontologo'


class Paciente(models.Model):
    rut_paciente = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    tipo_sangre = models.CharField(max_length=3, blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)
    sistema_salud = models.CharField(max_length=20, blank=True, null=True)
    ciudad = models.CharField(max_length=20, blank=True, null=True)
    calle = models.CharField(max_length=20, blank=True, null=True)
    numero_casa = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


class Radiografia(models.Model):
    id_documento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.BinaryField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_ficha = models.ForeignKey(FichaClinica, models.DO_NOTHING, db_column='id_ficha')

    class Meta:
        managed = False
        db_table = 'radiografia'


class RegistroDePago(models.Model):
    id_registro = models.AutoField(primary_key=True)
    boleta = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'registro_de_pago'


class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    id_ficha = models.ForeignKey(FichaClinica, models.DO_NOTHING, db_column='id_ficha')
    rut_odontologo = models.ForeignKey(Odontologo, models.DO_NOTHING, db_column='rut_odontologo', blank=True, null=True)
    id_registro = models.ForeignKey(RegistroDePago, models.DO_NOTHING, db_column='id_registro')
    descripcion = models.CharField(max_length=300, blank=True, null=True)
    presupuesto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento'


class Usa(models.Model):
    pk = models.CompositePrimaryKey('rut_odontologo', 'id_material')
    rut_odontologo = models.ForeignKey(Odontologo, models.DO_NOTHING, db_column='rut_odontologo')
    id_material = models.ForeignKey(Material, models.DO_NOTHING, db_column='id_material')
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usa'
