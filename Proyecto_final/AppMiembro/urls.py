from django.urls import path
from .views import *

urlpatterns=[
    path("saludar/", saludar),
    path("segunda_vista/",segunda_vista),
    path("dia/",dia_de_hoy),
    path("saludo/<nombre>",saludo_con_nombre,name="Saludo"),
    path("anio/<edad>",calcula_anio_nacimiento,name="Nacimiento"),
    
    #sitios 
    path("Sitio_principal/",Principal,name="Sitio_principal"),
    path("sitio/",Sitio_web,name="Sitio_web"),
    path("Colaboradores_site/",Colaboradores_site,name="Colaboradores_site"),
    path("Familiar_site/",Familiar_site,name="Familiar_site"),
    
    #ingresos a la bas de datos
    path("miembro/",familiar,name="familiar"),
    path("ingreso_colaborador/",Ing_colaborador,name="colaborado")
]