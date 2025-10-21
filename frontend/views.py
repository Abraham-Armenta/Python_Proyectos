from django.shortcuts import render

#esto de aqui es para llamarlo como tu quieras
def mostrar_frontend(request):
    return render(request, 'frontend.html') 

def contacto(request):
    return render(request, 'contacto.html')

def mostrar_about(request):
    return render(request, 'about.html')

