from django.shortcuts import render

# Create your views here.
def Pag1(request):
    return render(request,'happy/Pag1.html')

def Perros(request):
    return render(request,'happy/Perros.html')

def BañoEco(request):
    return render(request,'happy/BañoEco.html')

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