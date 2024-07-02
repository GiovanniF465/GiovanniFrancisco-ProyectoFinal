from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('login/',views.login, name='Login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'),name='Logout'),
    path('registro/',views.registro,name="Registro")
]
