from django.db import models

# Create your models here.
class Facultad(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

class Carrera(models.Model):
    name = models.CharField(max_length=45)
    abreviado = models.CharField(max_length=20)
    description = models.CharField(max_length=250)

class Alumno(models.Model):
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=55)
    semestre = models.IntegerField()
    telefono = models.CharField(max_length=9)
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=35)
    fecha_nac= models.DateTimeField()
    Genero = models.CharField(max_length=20)

class Comentario(models.Model):
    Comentario = models.CharField(max_length=750)
    fecha= models.DateTimeField()
    hora = models.TimeField()
#--------------------------------------------
class Publicacion(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=920)
    fecha= models.DateTimeField()
    hora = models.TimeField()
    vistas = models.IntegerField()

class Multimedia(models.Model):
    url = models.CharField(max_length=150)
    tipo= models.CharField(max_length=45)

#-----------------------------------------------
    class Intercambio(models.Model):
    universidad_destino = models.CharField(max_length=55)
    periodo = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    tipo= models.CharField(max_length=45)
    descripcion= models.CharField(max_length=450)
