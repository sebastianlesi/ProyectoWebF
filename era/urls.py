rom django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from era.models import Publicacion, Comentario
from era.forms import PublicacionForm, ComentarioForm
from era.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView

app_name = "era"

urlpatterns = [
    # List latest 5 restaurants: /myrestaurants/
    path('publicacion/create',
        PublicacionCreate.as_view(
            model=Publicacion,
            template_name='era/form.html',
            form_class=PublicacionForm),
        name='publicacion_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    path('publicacion/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Publicacion,
            form_class=PublicacionForm),
        name='publicacion_edit'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    path('publicacion/<int:pk>/comentario/create',
        ComentarioCreate.as_view(
            model=Comentario,
            template_name='era/form2.html',
            form_class=ComentarioForm),
        ),
        name='comentario_create'),

    # Edit restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1/edit/
    path('publicacion/<int:pkr>/comentario/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Comentario,
            form_class=ComentarioForm),
        name='comentario_edit'),
]