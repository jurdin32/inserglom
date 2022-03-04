from django.contrib import admin

# Register your models here.
from Inicio.models import *
from inserglom.snippers import Attr

@admin.register(SliderPrincipal)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(SliderPrincipal)
    list_display = Attr(SliderPrincipal)

@admin.register(QueHacemos)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(QueHacemos)
    list_display = Attr(QueHacemos)

@admin.register(RedesSociales)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(RedesSociales)
    list_display = Attr(RedesSociales)

@admin.register(NuestrosServicios)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(NuestrosServicios)
    list_display = Attr(NuestrosServicios)

@admin.register(Politicas)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Politicas)
    list_display = Attr(Politicas)

@admin.register(Certificaciones)
class modelo(admin.ModelAdmin):
    list_display_links = Attr(Certificaciones)
    list_display = Attr(Certificaciones)