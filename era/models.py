from django.db import models
from django.urls.base import reverse

# Create your models here.
class Facultad(models.Model):
    id_Facultad = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45)
    abreviado = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    Facultad_idFacultad = models.ForeignKey(Facultad, on_delete= models.CASCADE,default="1")

#-----------------------------------------------
class Intercambio(models.Model):
    id_intercambio = models.AutoField(primary_key=True, unique=True, editable=False)
    universidad_destino = models.CharField(max_length=55)
    periodo = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    tipo= models.CharField(max_length=45)
    descripcion= models.CharField(max_length=450)


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=55)
    semestre = models.IntegerField()
    telefono = models.CharField(max_length=9)
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=35)
    fecha_nac= models.DateTimeField()
    Genero = models.CharField(max_length=20)
    Carrera_idCarrera = models.ForeignKey(Carrera, on_delete = models.CASCADE ,default="1")
    Intercambio_idintercambio = models.ForeignKey(Intercambio, on_delete = models.CASCADE ,default="1")

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, unique=True, editable=False)
    Comentario = models.CharField(max_length=750)
    fecha= models.DateTimeField()
    hora = models.TimeField()
    Alumno_idalumno = models.ForeignKey(Alumno, on_delete = models.CASCADE,default="1")

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self) :
        return reverse('era:comentario_detail', kwargs={'pkr': self.publication.pk, 'pk':self.pk})

#--------------------------------------------
class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True, unique=True, editable=False)
    titulo = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=920)
    fecha= models.DateTimeField()
    hora = models.TimeField()
    vistas = models.IntegerField()
    Alumno_idAlumno = models.ForeignKey(Alumno,on_delete = models.CASCADE,default="1")

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self) :
        return reverse('era:publicacion_detail', kwargs={'pk': self.pk})

class Multimedia(models.Model):
    id_multimedia = models.AutoField(primary_key=True, unique=True, editable=False)
    url = models.CharField(max_length=150)
    tipo= models.CharField(max_length=45)
    Publicacion_idPublicacion = models.ForeignKey(Publicacion,on_delete = models.CASCADE,default="1")

    



        