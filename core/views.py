from django.shortcuts import render, redirect
from .forms import ContactoForm, DonacionForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from .models import Inicio, Nosotros, Programas, Actividades, Historias, Articulos, Donaciones, DonacionesCBU



def inicio(request):
    try:
        inicio_data = Inicio.objects.filter(publicado=True).latest('fecha_publicacion')
    except ObjectDoesNotExist:
        inicio_data = None  # o puedes asignar un valor por defecto o una estructura vacía

    return render(request, 'core/inicio.html', {'inicio': inicio_data})

def nosotros(request):
    try:
        nosotros_data = Nosotros.objects.filter(publicado=True).Nosotros.objects.latest('id')  # Obtener el último registro
    except Nosotros.DoesNotExist:
        nosotros_data = None
    
    return render(request, 'core/nosotros.html', {'nosotros': nosotros_data})

def programas(request):
    try:
        programas_data = Programas.objects.filter(publicado=True).Programas.objects.latest('id')
    except ObjectDoesNotExist:
        programas_data = None
        
    return render(request, 'core/programas.html', {'programas': programas_data})

def actividades(request):
    try:
        actividades_data = Actividades.objects.filter(publicado=True).Actividades.objects.all()
    except ObjectDoesNotExist:
        actividades_data = None
        
    return render(request, 'core/actividades.html', {'actividades': actividades_data})

def historias(request):
    try:
        historias_data = Historias.objects.filter(publicado=True).Historias.objects.all()
    except ObjectDoesNotExist:
        historias_data = None
    
    return render(request, 'core/historias.html', {'historias': historias_data})

def articulos(request):
    try:
        articulos_data = Articulos.objects.filter(publicado=True).Articulos.objects.all()
    except ObjectDoesNotExist:
        articulos_data = None
        
    return render(request, 'core/articulos.html', {'articulos': articulos_data})

#def donaciones_cbu(request):
#    donaciones_data_cbu = DonacionesCBU.objects.all()
#    return render(request, 'core/donaciones.html', {'donaciones_cbu':donaciones_data_cbu})

def donaciones(request):
    try:
        donaciones_data = Donaciones.objects.filter(publicado=True).Donaciones.objects.latest('id')  # Obtener el último registro de donaciones
    except ObjectDoesNotExist:
        donaciones_data = None
    
    try:
        donaciones_data_cbu = DonacionesCBU.objects.filter(publicado=True).DonacionesCBU.objects.all()
    except ObjectDoesNotExist:
        donaciones_data_cbu = None
    
    mensaje_exito = False
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y envía el correo electrónico
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'tu_correo@example.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                ['destino@example.com'],  # Cambia esto por el correo al cual enviarás el mensaje
                fail_silently=False,
            )
            mensaje_exito = True  # Marca como enviado exitosamente
            form = ContactoForm()  # Resetea el formulario
    else:
        form = ContactoForm()

    context = {
        'donaciones': donaciones_data,
        'donaciones_cbu': donaciones_data_cbu,
        'form': form,
        'mensaje_exito': mensaje_exito,
    }
    
    return render(request, 'core/donaciones.html', context)

def contacto(request):
    mensaje_exito = False  # Variable para indicar si se envió el formulario correctamente

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y envía el correo electrónico
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'tu_correo@example.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                ['destino@example.com'],  # Cambia esto por el correo al cual enviarás el mensaje
                fail_silently=False,
            )
            mensaje_exito = True  # Marca como enviado exitosamente
            form = ContactoForm()  # Resetea el formulario
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form, 'mensaje_exito': mensaje_exito})

