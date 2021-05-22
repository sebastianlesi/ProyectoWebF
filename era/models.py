from time import timezone
from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Facultad(models.Model):
    id_Facultad = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

class Carrera(models.Model):
    id_carrera = models.CharField(max_length=12)
    name = models.CharField(max_length=45)
    abreviado = models.CharField(max_length=20)
    description = models.TextField(max_length=250)
    Facultad_idFacultad = models.ForeignKey(Facultad, on_delete= models.CASCADE,null=True, related_name='carreras')

#-----------------------------------------------
class Intercambio(models.Model):
    id_intercambio = models.CharField(max_length=12)
    universidad_destino = models.CharField(max_length=55)
    periodo = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    tipo= models.TextField(max_length=45)
    descripcion= models.TextField(max_length=450)


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45, default="cholele")
    lastname = models.CharField(max_length=55, default= "hernandez")
    semestre = models.IntegerField(default=2, blank=True,null=True)
    telefono = models.CharField(max_length=9, null = True)
    correo = models.CharField(max_length=60, blank=True,null=True)
    clave = models.CharField(max_length=35, default="1234")
    fecha_nac= models.DateField(null=False, default=date.today)
    Genero = models.CharField(max_length=20, null=True)
    Carrera_idCarrera = models.ForeignKey(Carrera, on_delete = models.CASCADE,null=True, related_name='alumnos')
    Intercambio_idintercambio = models.ForeignKey(Intercambio, on_delete = models.CASCADE)

#--------------------------------------------
class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True, unique=True, editable=False)
    titulo = models.CharField(max_length=120) 
    descripcion = models.CharField(max_length=920, null = False, default="Movilidad en España")
    fecha= models.DateField(default=date.today)
    vistas = models.IntegerField(default="1")
    Alumno_idAlumno = models.ForeignKey(Alumno,on_delete = models.CASCADE,null=True, related_name='publicaciones')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")

    def __unicode__(self):
        return u"%s" % self.id_publicacion

    def get_absolute_url(self) :
        return reverse('era:publicacion_detail', kwargs={'pk': self.pk})

class Multimedia(models.Model):
    id_multimedia = models.CharField(max_length=120, default="1")
    url = models.CharField(max_length=150, null=True)
    tipo= models.CharField(max_length=45, null=True)
    Publicacion_idPublicacion = models.ForeignKey(Publicacion,on_delete = models.CASCADE,null=True, related_name='multimedias')

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True, unique=True, editable=False)
    Comentario = models.CharField(max_length=750, null=True)
    fecha= models.DateField(default=date.today)
    publicacion = models.ForeignKey(Publicacion,null=True,related_name='publicaciones',on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")


    def __unicode__(self):
        return u"%s" % self.id_comentario

    def get_absolute_url(self) :
        return reverse('era:comment_detail', kwargs={'pkr': self.publicacion.pk, 'pk':self.pk})

class Meta:
        abstract = True


#class Meta:
 #       unique_together = ("publicacion", "user")

    



        