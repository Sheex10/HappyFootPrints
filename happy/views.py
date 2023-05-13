from django.shortcuts import render

# Create your views here.
def Pag1(request):
    return render(request,'happy/Pag1.html')

def Perros(request):
    return render(request,'happy/Perros.html')

def Gatos(request):
    return render(request,'happy/Gatos.html')

def Razas(request):
    return render(request,'happy/Razas.html')

def Alfombra(request):
    return render(request,'happy/Alfombra.html')

def BañoEco(request):
    return render(request,'happy/BañoEco.html')

