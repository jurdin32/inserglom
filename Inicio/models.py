from django.db import models

# Create your models here.
class SliderPrincipal(models.Model):
    imagen=models.ImageField(upload_to='slider')
    texto1=models.CharField(max_length=100, null=True,blank=True)
    texto2=models.CharField(max_length=100, null=True,blank=True)
    estado=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="1. Slider Principal"


class QueHacemos(models.Model):
    texto=models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural="2. Lo que hacemos"

class RedesSociales(models.Model):
    facebook=models.CharField(max_length=200,blank=True,null=True)
    youtube=models.CharField(max_length=200,blank=True,null=True)
    linkedin=models.CharField(max_length=200,blank=True,null=True)
    twitter=models.CharField(max_length=200,blank=True,null=True)

    class Meta:
        verbose_name_plural="3. Redes Sociales"

class NuestrosServicios(models.Model):
    nombre_servicio=models.CharField(max_length=50, help_text=">Texto de no mas de 50 caracteres",null=True,blank=True)
    breve_descripcion=models.CharField(max_length=200, help_text=">Texto de no mas de 200 caracteres",null=True,blank=True)

    class Meta:
        verbose_name_plural="4. Nuestros Servicios"

class Politicas(models.Model):
    imagen=models.ImageField(upload_to='politicas')
    titulo=models.CharField(max_length=50, help_text="No mas de 50 caracteres")
    breve_descripcion=models.CharField(max_length=250,help_text="No mas de 250 caracteres")

    class Meta:
        verbose_name_plural="5. Políticas"

class Certificaciones(models.Model):
    titulo = models.CharField(max_length=50, help_text="No mas de 50 caracteres")
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural="6. Certificaciones"



