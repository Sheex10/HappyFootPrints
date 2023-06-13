from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Producto

# Create your views here.
def Pag1(request):
    return render(request,'happy/Pag1.html')

def Perros(request):

    return render(request,'happy/Perros.html')

def BañoEco(request):
    nombreB = "Baño Eco"
    precioB = 24.990
    descripcionB = "Baño Perro Puppy Potty Pad, es un espacio de aseo ecológico, perfecto para nuestras mascotas de compañía. Baño Ecológico para perros y mascotas."

    contexto = {
        "nombre" : nombreB,
        "precio" : precioB,
        "descripcion" : descripcionB
    }

    return render(request,'happy/BañoEco.html',contexto)

def Cama(request):

    return render(request,'happy/Cama.html')

def Casa(request):
    return render(request,'happy/Casa.html')

def Correa(request):
    return render(request,'happy/Correa.html')

def Juguete(request):
    return render(request,'happy/Juguete.html')

def Plato(request):
    return render(request,'happy/Plato.html')

def Gatos(request):
    return render(request,'happy/Gatos.html')

def Alfombra(request):
    return render(request,'happy/Alfombra.html')

def rascador(request):
    return render(request, 'happy/rascador.html')

def collar(request):
    return render(request,'happy/collar.html')

def CamaGatos(request):
    return render(request,'happy/CamaGatos.html')

def JugueteGato(request):
    return render(request,'happy/JugueteGato.html')

def Arenero(request):
    return render(request,'happy/Arenero.html')


def Razas(request):
    return render(request,'happy/Razas.html')

def Carrito(request):
    return render(request,'happy/Carrito.html')

def InicioSesion (request):
    return render(request,'happy/InicioSesion.html')

def IniAdmin (request):
    return render(request,'happy/IniAdmin.html')

def register (request):
    return render(request,'happy/register.html')

def Editar (request):
    return render(request,'happy/Editar.html')

def Editar2 (request):
    return render(request,'happy/Editar2.html')

def EditPerfil (request):
    return render(request,'happy/EditPerfil.html')

def Clave (request):
    return render(request,'happy/Clave.html')

def Clave2 (request):
    return render(request,'happy/Clave2.html')

def Admin (request):
    return render(request,'happy/Admin.html')

def Agregar(request):
    
    return render(request,'happy/Agregar.html')

def formProductos(request):
    vIdProd= request.POST['id']
    vDescripcion= request.POST['desc']
    vPeso= request.POST['peso']
    vPrecio= request.POST['precio']
    vFoto=request.FILES['foto']


    Producto.objects.create(id_producto=vIdProd, descripcion=vDescripcion, peso=vPeso, precio=vPrecio, fotoProd=vFoto)

    return redirect('Agregar')


