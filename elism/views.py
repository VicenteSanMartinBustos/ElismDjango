from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm


# Create your views here.

#vistas de los links
def register(request):
    return render(request, 'register.html')

def iniciarSesion(request):
    return render(request, 'iniciarSesion.html')

def index(request):
    return render(request, 'index.html')

def ropa(request):
    return render(request, 'ropa.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def carrito(request):
    return render(request, 'carrito.html')



# bdd de los productos
def ropa(request):
    productos = Producto.objects.all()
    return render(request, 'ropa.html', {'products': productos})


class ProductoListView(ListView):
    model = Producto
    template_name = 'producto_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'precio', 'imagen']

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto_form.html'
    fields = ['nombre', 'precio', 'imagen']

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


def iniciarSesion(request):
    if request.method == 'GET':
        return render(request, "iniciarSesion.html", {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
        return render(request, "iniciarSesion.html", {'form': form, 'error': "Usuario y/o contraseña incorrecta."})

def register(request):
    if request.method == 'GET':
        return render(request, "register.html", {'form': RegistroForm()})
    else:
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "register.html", {'form': RegistroForm(), 'success': "Registro completo."})
        else:
            return render(request, "register.html", {'form': form, 'error': "Errores en el formulario."})

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')