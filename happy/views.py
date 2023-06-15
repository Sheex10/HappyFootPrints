from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Producto, Usuario

# Create your views here.
def Pag1(request):
    return render(request,'happy/Pag1.html')

def Perros(request):

    return render(request,'happy/Perros.html')

def BañoEco(request):
    nombreB = "Baño Eco"
    precioB = "PRECIO : $24.990"
    descripcionB = "Baño Perro Puppy Potty Pad, es un espacio de aseo ecológico, perfecto para nuestras mascotas de compañía. Baño Ecológico para perros y mascotas."

    contexto = {
        "nombre" : nombreB,
        "precio" : precioB,
        "descripcion" : descripcionB
    }

    return render(request,'happy/BañoEco.html',contexto)

def Cama(request):
    nombreC = "Cama antiestres"
    precioC = "PRECIO : $30.990"
    descripcionC = "La cama antiestrés -100-120cm- Damasco disponibles en diferentes tamaños.Esta cama calmante tiene un tejido especial de suave felpa, para que tu mascota esté comoda y relajada."

    contexto = {
        "nombre" : nombreC,
        "precio" : precioC,
        "descripcion" : descripcionC
    }
    return render(request,'happy/Cama.html',contexto)

def Casa(request):
    nombreCP = "Casa plastica"
    precioCP = "PRECIO : $68.990"
    descripcionCP = "Casa para perros diseñada de un tamaño ideal para razas de tamaño mediano o grandes. Tiene un piso elevado para aislar al canino y también seguro. Su material es resistente a la humedad, y es sencillo de limpiar. Protección de rayos UV."

    contexto = {
        "nombre" : nombreCP,
        "precio" : precioCP,
        "descripcion" : descripcionCP
    } 
    return render(request,'happy/Casa.html',contexto)

def Correa(request):
    nombreCO = "Correa de paseo"
    precioCO = "PRECIO : $8.990"
    descripcionCO = "Hecha de poliester suave y duradero, la correa para perros Atlanta es super suave en las manos y viene con un gancho que se puede bloquear para una experiencia segura."
    
    contexto = {
        "nombre" : nombreCO,
        "precio" : precioCO,
        "descripcion" : descripcionCO
    }

    return render(request,'happy/Correa.html',contexto)

def Juguete(request):
    nombreJ = "Juguete de perro"
    precioJ = "PRECIO : $5.490"
    descripcionJ = "Hecho de algodón natural con fibras vegetales. Cuerda colorida co pelota incluida perfecta para los animales que muerden constantemente, ya que ayuda a la dentadura del perro."

    contexto = {
        "nombre" : nombreJ,
        "precio" : precioJ,
        "descripcion" : descripcionJ
    }
    return render(request,'happy/Juguete.html',contexto)

def Plato(request):
    nombreP = "Comedero y Bebedero"
    precioP = "PRECIO : $8.990"
    descripcionP = "Bonve Pet 2x400ML. Comedero para perros de acero inoxidable con base de silicona antideslizante, 2 cuencos comedero para comida y agua."

    contexto = {
        "nombre" : nombreP,
        "precio" : precioP,
        "descripcion" : descripcionP
    }
    return render(request,'happy/Plato.html',contexto)

def Gatos(request):
    return render(request,'happy/Gatos.html')

def Alfombra(request):
    nombreAl = "Alfombra Sanitaria"
    precioAl = "PRECIO: $10.990"
    descripcionAl = "La almohadilla de arena para gatos puede mantener el suelo limpio y su casa libre de malos olores. Evita que la arena ingrese al piso y lo mantiene limpio."

    contexto = {
        "nombre" : nombreAl,
        "precio" : precioAl,
        "descripcion" : descripcionAl
    }
    return render(request,'happy/Alfombra.html',contexto)

def rascador(request):
    nombreR = "Rascador de 3 niveles"
    precioR = "PRECIO: $47.990"
    descripcionR = "Rascador de 3 niveles de 90 cm con distintos juguetes,casitas y dos hamacas que le ayudarán a tu gato a tener un mejor descanso y 	experiencia."
    
    contexto = {
        "nombre" : nombreR,
        "precio" : precioR,
        "descripcion" : descripcionR
    }

    return render(request, 'happy/rascador.html',contexto)

def collar(request):
    nombreCollar = "Collar para gatos naranjo"
    precioCollar = "PRECIO: $5.990"
    descripcionCollar= "Collar color naranjo con distintas lineas celestes. Su tela es bastante comoda y no le va a incomodar, y es ajustable."

    contexto = {
		"nombre" : nombreCollar,
		"precio" : precioCollar,
		"descripcion" : descripcionCollar
}
    return render(request,'happy/collar.html',contexto)

def CamaGatos(request):
    nombreCGA = "Cama en forma de iglú café"
    precioCGA = "PRECIO: $23.990"
    descripcionCGA = "La cama en forma de iglú es muy comoda y agradable, especialmente 	diseñada para tu felino. Esta forma es ideal para generar amyor comodidad y 	tranquilidad a la hora de dormir"

    contexto = {
		"nombre" : nombreCGA,
		"precio" : precioCGA,
		"descripcion" : descripcionCGA
}
    return render(request,'happy/CamaGatos.html',contexto)

def JugueteGato(request):
    nombreJu = "Juguete loco rosado"
    precioJu = "PRECIO: $2.390"
    descripcionJu = "Juguete en forma de huevo incentiva a nuestros gatos a jugar y moverse continuamente. Tiene plumas y un cascabel para mantener curioso al gato."

    contexto = {
		"nombre" : nombreJu,
		"precio" : precioJu,
		"descripcion" : descripcionJu 
}
    return render(request,'happy/JugueteGato.html',contexto)

def Arenero(request):
        nombreAr = "Arenero con techo"
        precioAr = "PRECIO : $15.990"
        descripcionAr = "Baño sanitario para gatos, incluyendo techo para mayor privacidad de tu felino para que no salga el mal olor hacia el exterior."

        contexto = {
            "nombre" : nombreAr,
            "precio" : precioAr,
            "descripcion" : descripcionAr
        }
    
        return render(request,'happy/Arenero.html',contexto)


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

def administrativo (request):
    return render(request,'happy/administrativo.html')

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

def formSesion(request):
    vUsuario = request.POST['usuario']
    vContraseña = request.POST['password']

    Usuario.objects.create(correo=vUsuario, clave=vContraseña)

    return redirect('Pag1')
#--

