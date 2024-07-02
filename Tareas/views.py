from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tarea
from .forms import TareaForm

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/index.html'
    context_object_name = 'tareas'
    ordering = ['-creada']

class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tareas/detalles_tarea.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_nueva.html'
    success_url = reverse_lazy('Listado')

class TareaUpdateView(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/editar_tarea.html'
    success_url = reverse_lazy('Listado')
    
class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/confirmarEliminar_tarea.html'
    success_url = reverse_lazy('Listado')

class TareaCompleteView(UpdateView):
    model = Tarea
    fields = ['completada']
    template_name = 'tareas/completar_tarea.html'
    success_url = reverse_lazy('Listado')

    def form_valid(self, form):
        form.instance.completada = True
        return super().form_valid(form)