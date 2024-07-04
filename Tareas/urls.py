from django.urls import path
from .views import (
    ListadoTareaView, 
    DetalleTareaView, 
    CrearTareaView, 
    ActualizarTareaView, 
    CompletarTareaView,
    EliminarTareaView
)

urlpatterns = [
    path('', ListadoTareaView.as_view(), name='Listado'),
    path('tarea/<int:pk>/', DetalleTareaView.as_view(), name='Detalles'),
    path('nueva_tarea/', CrearTareaView.as_view(), name='Nueva'),
    path('editar_tarea/<int:pk>/', ActualizarTareaView.as_view(), name='Editar'),
    path('completar/<int:pk>/', CompletarTareaView.as_view(), name='Completar'),
    path('eliminar/<int:pk>/', EliminarTareaView.as_view(), name='Eliminar'),
]