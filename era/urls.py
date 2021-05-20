from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView

from era.forms import PublicacionForm, ComentarioForm
from era.models import Publicacion, Comentario
#from era.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView

app_name = "era"

urlpatterns = [


    ##  -----------------Publications-----------------------------------
    #Registrar un pubblicacion, de: /era/Create
    path('publicacion/create',
        CreateView.as_view(
            model=Publicacion,
            template_name='era/form.html',
            form_class=PublicacionForm),
        name='publicacion_create'),
    
    #Publicacion details, /myrestaurants/1
    path('publicaciones/<int:pk>',
        DetailView.as_view(
            model=Publicacion,
            template_name='era/publicacion_detail.html'),
        name='publicacion_detail'),




    ##  -----------------Comments-----------------------------------
     # Create a publication comment, ex.: /era/publicaciones/1/comments/create/
    path('publicaciones/<int:pk>/comment/create',
        CreateView.as_view(
            model=Comentario,
            template_name='era/form.html',
            form_class=ComentarioForm),
        name='comment_create'),

    # Publication comment details, ex: /era/Publication/1/comments/1/
    path('publications/<int:pkr>/comments/<int:pk>',
        CreateView.as_view(
            model=Comentario,
            template_name='era/comentario_detail.html'),
        name='comentario_detail'),
]