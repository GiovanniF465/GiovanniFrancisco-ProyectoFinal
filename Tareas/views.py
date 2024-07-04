from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms import TareaForm

class ListadoTareaView(ListView):
    model = Tarea
    template_name = 'tareas/index.html'
    context_object_name = 'tareas'
    ordering = ['-creada']
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user).order_by('-creada')

class DetalleTareaView(DetailView):
    model = Tarea
    template_name = 'tareas/detalles_tarea.html'
    context_object_name = 'tarea'
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

class CrearTareaView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_nueva.html'
    success_url = reverse_lazy('Listado')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ActualizarTareaView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editar_tarea.html'
    success_url = reverse_lazy('Listado')
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)
    
class EliminarTareaView(DeleteView):
    model = Tarea
    template_name = 'tareas/confirmarEliminar_tarea.html'
    success_url = reverse_lazy('Listado')
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)

class CompletarTareaView(UpdateView):
    model = Tarea
    fields = ['completada']
    template_name = 'tareas/completar_tarea.html'
    success_url = reverse_lazy('Listado')

    def form_valid(self, form):
        form.instance.completada = True
        return super().form_valid(form)
    
    def get_queryset(self):
        return Tarea.objects.filter(usuario=self.request.user)