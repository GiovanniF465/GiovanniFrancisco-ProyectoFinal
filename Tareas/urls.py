from django.urls import path
from Tareas import views

urlpatterns = [
    path('',views.listado_tareas,name="Listado"),
    path('nueva_tarea/',views.tarea_nueva,name="Nueva")
]

