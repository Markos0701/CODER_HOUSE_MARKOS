from django.urls import path
from .views import *

urlpatterns=[
    path("saludar/", saludar),
    path("segunda_vista/",segunda_vista),
    path("dia/",dia_de_hoy),
    path("saludo/<nombre>",saludo_con_nombre,name="Saludo"),
    path("anio/<edad>",calcula_anio_nacimiento,name="Nacimiento"),
    path("sitio/",Sitio_web,name="Sitio_web"),
    path("miembro/",familiar,name="familiar"),
    path("Sitio_web2/",Sitio_web2,name="Sitio_web2"),
    path("",Inicio,name="Inicio"),

]