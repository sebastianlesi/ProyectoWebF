from django.forms import ModelForm
from era.models import Publicacion, Comentario

class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        exclude = ('titulo', 'Descripcion', 'Vistas',)

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        exclude = ('comentario',)