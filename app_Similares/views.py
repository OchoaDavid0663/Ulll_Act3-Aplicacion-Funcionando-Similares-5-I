from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.http import HttpResponse # Importa HttpResponse para casos de depuración o confirmación simple
from django.views.decorators.http import require_POST

# --- VISTAS PARA CLIENTES ---

def inicio_similares(request):
    """
    Vista para la página de inicio del sistema.
    """
    return render(request, 'app_Similares/inicio.html')

def ver_clientes(request):
    """
    Muestra una lista de todos los clientes registrados.
    """
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'app_Similares/clientes/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    """
    Maneja la adición de un nuevo cliente.
    Si la solicitud es GET, muestra el formulario.
    Si la solicitud es POST, procesa los datos del formulario y guarda el cliente.
    """
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')

        # Simple validación, se puede mejorar
        if nombre and apellido and email:
            # Crea un nuevo cliente
            Cliente.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                direccion=direccion,
                fecha_nacimiento=fecha_nacimiento if fecha_nacimiento else None
            )
            return redirect('ver_clientes') # Redirige a la lista de clientes después de agregar
        else:
            # Si faltan datos importantes, puedes añadir un mensaje de error
            return render(request, 'app_Similares/clientes/agregar_clientes.html', {
                'error_message': 'Por favor, completa todos los campos obligatorios.'
            })
    return render(request, 'app_Similares/clientes/agregar_clientes.html')


def actualizar_cliente(request, pk):
    """
    Muestra el formulario para actualizar un cliente existente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'app_Similares/clientes/actualizar_clientes.html', {'cliente': cliente})

@require_POST
def realizar_actualizacion_cliente(request, pk):
    """
    Procesa los datos del formulario POST para actualizar un cliente existente.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    
    cliente.nombre = request.POST.get('nombre')
    cliente.apellido = request.POST.get('apellido')
    cliente.email = request.POST.get('email')
    cliente.telefono = request.POST.get('telefono')
    cliente.direccion = request.POST.get('direccion')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    cliente.fecha_nacimiento = fecha_nacimiento if fecha_nacimiento else None
    
    cliente.save() # Guarda los cambios en la base de datos
    return redirect('ver_clientes') # Redirige a la lista de clientes

def borrar_cliente(request, pk):
    """
    Muestra la página de confirmación para borrar un cliente (GET)
    y luego borra el cliente si se confirma con POST.
    """
    cliente = get_object_or_404(Cliente, pk=pk)
    
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    
    # Si es GET, muestra la página de confirmación
    return render(request, 'app_Similares/clientes/borrar_cliente.html', {'cliente': cliente})