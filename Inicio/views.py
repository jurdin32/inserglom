from django.shortcuts import render

# Create your views here.
from Inicio.models import SliderPrincipal, QueHacemos, RedesSociales, NuestrosServicios, Politicas, Certificaciones


def index(request):
    sliders=SliderPrincipal.objects.all()
    contexto={
        'slider':sliders,
        'contador':sliders.count()*"*",
        'quehacemos':QueHacemos.objects.all(),
        'redes':RedesSociales.objects.first(),
        'servicios':NuestrosServicios.objects.all(),
        'politicas':Politicas.objects.all(),
        'certificaciones':Certificaciones.objects.all(),
    }
    return render(request,"index.html",contexto)