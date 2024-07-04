from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormCreacion, EditarPerfil
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

def inicio(request):
    return render(request,'usuarios/principal.html')


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(request,username=usuario,password=contrasenia)
            
            django_login(request,user)
            
            DatosExtra.objects.get_or_create(user=user)
            
            return redirect('Listado')
    
    return render(request,'usuarios/login.html', {'formulario':formulario})

def registro(request):
    formulario = FormCreacion()
    if request.method == "POST":
        formulario = FormCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Login')
    
    return render(request, 'usuarios/registro.html', {'formulario':formulario})

@login_required
def verPerfil(request):
    usuario = request.user
    datos_extra = usuario.datosextra
    
    return render(request, 'usuarios/ver_perfil.html', {'usuario': usuario, 'datos_extra': datos_extra})


@login_required
def editar_perfil(request):
    usuario = request.user
    datos_extra = usuario.datosextra
    formulario = EditarPerfil(instance=usuario)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES, instance=usuario)
        
        if formulario.is_valid():
            formulario.save()
            
            if 'avatar' in request.FILES:
                datos_extra.avatar = request.FILES['avatar']
                datos_extra.save()
            
            return redirect('VerPerfil') 
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})


class cambiarPassword(LoginRequiredMixin,PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('Editar')

def about(request):
    return render(request, 'usuarios/about.html')