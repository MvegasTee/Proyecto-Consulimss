from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import EquipoForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio o donde desees
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'login.html')


# Vista para el Dashboard
@login_required  # Solo los usuarios logueados pueden ver esta página
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def ingresar_datos(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige al Dashboard después de guardar
    else:
        form = EquipoForm()
    return render(request, 'ingresar_datos.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html')
