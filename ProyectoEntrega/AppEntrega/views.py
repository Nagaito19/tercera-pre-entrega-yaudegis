from django.shortcuts import render,redirect
from AppEntrega.models import *
from AppEntrega.forms import *
from django.http import HttpResponse



def inicio(request):
    return render(request, "AppEntrega/inicio.html")

def estilo(request):
    mi_estilo=Estilo.objects.all()

    if request.method =='POST':
        mi_formulario=EstiloFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            estilo=Estilo(nombre=informacion['estilo'])
            estilo.save()
            nuevo_estilo={'nombre':informacion['estilo']}
            return render(request,'AppEntrega\estilo.html', {'formulario_estilo':mi_estilo,
                                                            'nuevo_estilo':nuevo_estilo,
                                                            'mi_estilo':mi_estilo})
    else:
        mi_formulario=EstiloFormulario()

    return render(request, "AppEntrega\estilo.html", {'formulario_estilo':mi_formulario,'mi_estilo':mi_estilo})

def truco (request):
    mi_truco=Truco.objects.all()

    if request.method =='POST':
        mi_formulario=TrucoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            truco=Truco(nombre=informacion['truco'], clase=informacion['truco'])
            truco.save()
            nuevo_truco={'nombre':informacion['truco']}
            return render(request,'AppEntrega\truco.html', {'formulario_truco':mi_truco,
                                                            'nuevo_truco':nuevo_truco,
                                                            'mi_truco':mi_truco})
    else:
        mi_formulario=TrucoFormulario()

    return render(request, "AppEntrega\truco.html", {'formulario_truco':mi_formulario,'mi_truco':mi_truco})
def mago (request):
    return render(request, "AppEntrega/mago.html")

def estilo_formularios(request):

    if request.method == 'POST':
        mi_formulario=EstiloFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_estilo=Estilo(nombre=request.POST['estilo'])
            nuevo_estilo.save()
            return redirect('/AppEntrega/')
    mi_formulario= EstiloFormulario()
    return render(request,'AppEntrega/estilo-formularios.html', {"formulario_estilo":mi_formulario})

def mago_formularios(request):
    
    if request.method == 'POST':
        mi_formulario=MagoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_mago=Mago(nombre=informacion['nombre'],
                            apellido=informacion['apellido'])
            nuevo_mago.save()
            return redirect('/AppEntrega/')
    mi_formulario= MagoFormulario()
    return render(request,'AppEntrega/Mago-formularios.html', {"formulario_mago":mi_formulario})

def truco_formularios(request):
    
    if request.method == 'POST':
        mi_formulario=TrucoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            nuevo_truco=Truco(nombre=informacion['nombre'],
                              clase=informacion['clase'])
            nuevo_truco.save()
            return redirect('/AppEntrega/')
    mi_formulario= TrucoFormulario()
    return render(request,'AppEntrega/truco-formularios.html', {"formulario_truco":mi_formulario})

def busqueda_magos(request):
    nombre_busqueda = request.GET.get('nombre')
    if nombre_busqueda:
         magos = Mago.objects.filter(nombre__icontains=nombre_busqueda)
    else:
        magos = Mago.objects.all()
    
    form = BusquedaMago()
    return render(request,'AppEntrega/listado-magos.html', {"listado_magos":magos, 'form': form})