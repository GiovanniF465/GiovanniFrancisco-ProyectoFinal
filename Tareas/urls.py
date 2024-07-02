from django.urls import path
from .views import (
    TareaListView, 
    TareaDetailView, 
    TareaCreateView, 
    TareaUpdateView, 
    TareaCompleteView,
    TareaDeleteView
)

urlpatterns = [
    path('', TareaListView.as_view(), name='Listado'),
    path('tarea/<int:pk>/', TareaDetailView.as_view(), name='Detalles'),
    path('nueva_tarea/', TareaCreateView.as_view(), name='Nueva'),
    path('editar_tarea/<int:pk>/', TareaUpdateView.as_view(), name='Editar'),
    path('completar/<int:pk>/', TareaCompleteView.as_view(), name='Completar'),
    path('eliminar/<int:pk>/', TareaDeleteView.as_view(), name='Eliminar'),
]