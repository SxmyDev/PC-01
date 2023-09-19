from django.shortcuts import redirect, render
from .models import *
from .forms import TareaForm, ProductoForm

def home(request):
    tareas = Tarea.objects.all()
    productos = Producto.objects.all()
    context = {'tareas' : tareas, 'productos' : productos}
    return render(request, 'mycrud/home.html', context)

def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm()
    context = {'form' : form}
    return render(request, 'mycrud/agregar_tarea.html', context)

def eliminar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('home')

def editar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TareaForm(instance=tarea)
    context = {'form': form, 'tarea': tarea}
    return render(request, 'mycrud/editar_tarea.html', context)


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    context = {'form' : form}
    return render(request, 'mycrud/agregar_producto.html', context)

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('home')

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)
    context = {'form': form, 'producto': producto}
    return render(request, 'mycrud/editar_producto.html', context)