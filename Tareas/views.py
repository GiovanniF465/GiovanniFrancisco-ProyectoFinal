from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def listado_tareas(request):
    tareas = Tarea.objects.all()
    return render(request,'tareas/index.html', {'tareas':tareas})

def tarea_nueva(request):
    if request.method == 'POST':
        formulario = TareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listado')
    else:
        formulario = TareaForm()
    return render(request,'tarea_nueva.html',{'formulario':formulario})    