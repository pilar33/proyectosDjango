from django.shortcuts import render

# Create your views here.
def Inicio(request):
    # le indicamos a la vista que pagina renderizar ante la solicitud del usuario 
    return render(request, "index.html")

def Contacto(request):
    return render(request, "contacto.html")