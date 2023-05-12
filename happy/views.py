from django.shortcuts import render

# Create your views here.
def Pag1(request):
    return render(request,'happy/Pag1.html')

def Perros(request):
    return render(request,'happy/Perros.html')

