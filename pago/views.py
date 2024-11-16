from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from descuento.models import Descuento
from .models import Pago
from django.contrib import messages 
from django.contrib.auth.models import User
from usuarioPadreFamilia.models import UsuarioPadreFamilia
from cronograma.models import Cronograma

def pagina_principal(request):
    if request.user.is_authenticated:
        return render(request, 'pagina_principal.html') 

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pagina_principal') 
        else:
            messages.error(request, 'Credenciales incorrectas')

    return render(request, 'pagina_principal.html')  

@login_required
def procesar_pago(request):
    if request.method == 'POST':
        valor_pago = request.POST.get('valor_pago')
        tipo_pago = request.POST.get('tipo_pago')
        nuevo_pago = Pago(valor_pago=valor_pago, tipo_pago=tipo_pago, estado_pago='PENDIENTE')
        nuevo_pago.save()
        
        messages.success(request, 'Pago procesado exitosamente.')
        return redirect('pagina_principal')  
    return render(request, 'procesar_pago.html')
def usuario_padre_familia_edit_view(request):
    # Lógica de la vista
    return render(request, 'pago/editar_usuario.html')
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuario creado con éxito.')
            return redirect('pagina_principal') 
        except Exception as e:
            messages.error(request, f'Error al crear el usuario: {str(e)}')
    
    return render(request, 'crear_usuario.html')

def pago_pendiente(request):
    descuentos = Descuento.objects.all()
    cronogramas = Cronograma.objects.all()
    usuarios = UsuarioPadreFamilia.objects.all()

    return render(request, 'pago_pendiente.html', {'descuentos': descuentos, 'cronogramas': cronogramas, 'usuarios': usuarios})

def pago_pendiente(request):
    descuentos = Descuento.objects.all()
    cronogramas = Cronograma.objects.all()
    usuarios = UsuarioPadreFamilia.objects.all()

    if request.method == 'POST':
        nombre_pago = request.POST.get('nombre_pago')
        valor_pago = request.POST.get('valor_pago')
        fecha_pago = request.POST.get('fecha_pago')
        tipo_pago = request.POST.get('tipo_pago')

        descuento_id = request.POST.get('descuentos')
        cronograma_id = request.POST.get('cronograma')
        usuario_id = request.POST.get('usuario')

        # Obtener las instancias seleccionadas
        descuento = Descuento.objects.get(id=descuento_id) if descuento_id else None
        cronograma = Cronograma.objects.get(id=cronograma_id) if cronograma_id else None
        usuario = UsuarioPadreFamilia.objects.get(id=usuario_id) if usuario_id else None

        # Crear el nuevo pago
        nuevo_pago = Pago(
            nombre_pago=nombre_pago,
            valor_pago=valor_pago,
            fecha_pago=fecha_pago,
            tipo_pago=tipo_pago,
            estado_pago='PENDIENTE',
            cronograma=cronograma,
            usuario_padre=usuario
        )
        nuevo_pago.save()

        # Asociar el descuento al pago
        if descuento:
            nuevo_pago.descuentos.add(descuento)

        messages.success(request, 'Pago pendiente agregado exitosamente.')
        return redirect('/')  # Redirigir después de guardar

    return render(request, 'pago_pendiente.html', {
        'descuentos': descuentos,
        'cronogramas': cronogramas,
        'usuarios': usuarios
    })