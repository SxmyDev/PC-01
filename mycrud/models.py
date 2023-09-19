from django.db import models

ESTADOS = (
    ('pendiente', 'Pendiente'),
    ('completada', 'Completada'),
)

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return self.titulo

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_productos/')
    
    def __str__(self):
        return self.nombre