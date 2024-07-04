from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('login/',views.login, name='Login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'),name='Logout'),
    path('registro/',views.registro,name="Registro"),
    path('perfil/',views.verPerfil,name="VerPerfil"),
    path('about/',views.about,name="About"),
    path('perfil/editar/', views.editar_perfil,name="Editar"),
    path('perfil/editar/cambiar_password/',views.cambiarPassword.as_view(), name='CambiarPass')
]
