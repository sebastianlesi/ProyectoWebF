from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from era.models import Publicacion, Comentario
from era.forms import PublicacionForm, ComentarioForm

# Security Mixins

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'registration/form.html'

# HTML Views

#-------------------------Publicacion----------------------------
class PublicacionCreate(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'registration/form.html'
    form_class = PublicacionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PublicacionCreate, self).form_valid(form)


class PublicacionDetail(DetailView):
    model = Publicacion
    template_name = 'era/publicacion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PublicacionDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context


#-------------------------Comentario----------------------------
class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comentario
    template_name = 'registration/form.html'
    form_class = ComentarioForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.publicacion = Publicacion.objects.get(id=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)

class CommentDetail(DetailView):
    model = Comentario
    template_name = 'era/comentario_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommentDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

@login_required()
def review(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(publicacion.id,)))
