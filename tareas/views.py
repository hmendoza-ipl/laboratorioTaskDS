from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


# Funcion auxiliar para comprobar si el usuario es admin

def es_admin(user):
    return user.groups.filter(name='Admin').exists()

@login_required # si no está logueado, lo redirige al login

def dashboard(request):
    # pasamos el usuario logueado al HTML
    return render(request, 'dashboard.html', {'usuario': request.user})

@login_required
@user_passes_test(es_admin) # Solo pasa si la funcion es_admin devuelve True

def crear_proyecto(request):
    return HttpResponse("Bienvenido Admin. Aquí podrás crear proyectos)")