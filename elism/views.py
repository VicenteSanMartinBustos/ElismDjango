from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

# Vistas de los links
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


def index(request):
    return render(request, "index.html")

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('iniciarSesion')

def ropa(request):
    productos = Producto.objects.all()
    return render(request, 'ropa.html', {'productos': productos})

def nosotros(request):
    return render(request, 'nosotros.html')

def carrito(request):
    return render(request, 'carrito.html')

def crud(request):
    return render(request, 'crud.html')

def proceder_al_pago(request):
    return render(request, 'proceder_al_pago.html')



# views.py
from django.http import JsonResponse
from .models import Contacto
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def guardar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        correo_electronico = request.POST.get('email')
        mensaje = request.POST.get('message')

        contacto = Contacto(nombre=nombre, correo_electronico=correo_electronico, mensaje=mensaje)
        contacto.save()

        return JsonResponse({'status': 'success', 'message': 'Formulario enviado correctamente.'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

def crud(request):
    productos = Producto.objects.all()
    return render(request, 'crud.html', {'productos': productos})

def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            return redirect('crud')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('crud')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('crud')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})


from django.shortcuts import render
from .models import Producto
from django.core.paginator import Paginator


def crud(request):
    query = request.GET.get('q', '')  # Proporciona un valor por defecto de cadena vacía
    productos = Producto.objects.all()

    if query:
        productos = productos.filter(nombre__icontains=query)

    paginator = Paginator(productos, 3)  # Muestra 5 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'crud.html', {'productos': page_obj, 'query': query})





# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(
        usuario=request.user, 
        producto=producto,
        defaults={'cantidad': 1}
    )
    if not created:
        carrito.cantidad += 1
        carrito.save()
    return redirect('carrito')

@login_required
def carrito(request):
    carritos = Carrito.objects.filter(usuario=request.user)
    total = sum(carrito.subtotal() for carrito in carritos)
    return render(request, 'carrito.html', {'carritos': carritos, 'total': total})

@login_required
def eliminar_del_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id, usuario=request.user)
    carrito.delete()
    return redirect('carrito')

@login_required
def proceder_al_pago(request):
    # Aquí agregarías la lógica para proceder al pago.
    return render(request, 'proceder_al_pago.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Producto, Carrito

@login_required
def carrito(request):
    try:
        carrito_items = Carrito.objects.filter(usuario=request.user)
        total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    except Exception as e:
        print(f"Error: {e}")
        carrito_items = []
        total = 0

    context = {
        'carrito_items': carrito_items,
        'total': total,
    }
    return render(request, 'carrito.html', context)





