from django.urls import path
from .views import *

urlpatterns=[

    path("saludar/", saludar),
    path("segunda_vista/",segunda_vista),
    path("dia/",dia_de_hoy),
    path("saludo/<nombre>",saludo_con_nombre,name="Saludo"),
    path("anio/<edad>",calcula_anio_nacimiento,name="Nacimiento"),
    
    #sitios 
    path("",Principal,name="Sitio_principal"),
    path("Sitio_principal/",Principal,name="Sitio_principal"),
    path("sitio/",Sitio_web,name="Sitio_web"),
    path("Colaboradores_site/",Colaboradores_site,name="Colaboradores_site"),
    path("Colaborador_site/",Colaborador_site,name="Colaborador_site"),
    path("Familiar_site/",Familiar_site,name="Familiar_site"),
    path("Producto_site/",Producto_site,name="Producto_site"),

    #ingresos a la base de datos

    path("miembro/",familiar,name="familiar"),
    path("ingreso_colaborador/",Ing_colaborador,name="colaborado"),
    path("ingreso_producto/",Ing_producto,name="ing_producto"),
    path("Producto_Busqueda/",Producto_Busqueda,name="Producto_Busqueda"),

]