from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView

from era.forms import PublicacionForm, ComentarioForm
from era.models import Publicacion, Comentario
from era.views import CommentDetail, PublicacionCreate, CommentCreate, PublicacionDetail, LoginRequiredCheckIsOwnerUpdateView

app_name = "era"

urlpatterns = [


    ##  -----------------Publications-----------------------------------
    #Registrar un pubblicacion, de: /era/Create
    path('publicacion/create',
        PublicacionCreate.as_view(
            model=Publicacion,
            template_name='era/form.html',
            form_class=PublicacionForm),
        name='publicacion_create'),
    
    #Publicacion details, /myrestaurants/1
    path('publicacion/<int:pk>',
        PublicacionDetail.as_view(
            model=Publicacion,
            template_name='era/publicacion_detail.html'),
        name='publicacion_detail'),

    # Edit publication details, ex.: /era/publications/1/edit/
    path('publicacion/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Publicacion,
            form_class=PublicacionForm),
        name='publicacion_edit'),


    ##  -----------------Comments-----------------------------------
     # Create a publication comment, ex.: /era/publicaciones/1/comments/create/
    path('publicacion/<int:pk>/comment/create',
        CommentCreate.as_view(
            model=Comentario,
            template_name='era/form.html',
            form_class=ComentarioForm),
        name='comment_create'),

    # Publication comment details, ex: /era/Publication/1/comments/1/
    path('publicacion/<int:pkr>/comment/<int:pk>',
        CommentDetail.as_view(
            model=Comentario,
            template_name='era/comentario_detail.html'),
        name='comment_detail'),

    # Edit publication comment details, ex.: /era/publications/1/comments/1/edit/
    path('publicacion/<int:pkr>/comment/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Comentario,
            form_class=ComentarioForm),
        name='comment_edit'),
]