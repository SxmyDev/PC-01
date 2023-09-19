from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_tarea/', views.agregar_tarea, name='agregar_tarea'),
    path('eliminar_tarea/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('editar_tarea/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
]