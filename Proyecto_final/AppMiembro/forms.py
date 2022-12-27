from django import forms

class ColaboradorForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    apellido= forms.CharField(label="Apellido:",max_length=50)
    dni= forms.IntegerField(label="DNI:",)
    cargo= forms.CharField(label="cargo:",max_length=50)
    fecha_ingreso= forms.DateField(label="fecha_ingreso:",widget=forms.SelectDateWidget(years=range(1940, 2030)))
    
class ProductoForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    marca= forms.CharField(label="marca:",max_length=50)
    codigo= forms.IntegerField(label="codigo:",)
    cantidad= forms.CharField(label="cantidad:",max_length=50)
    
    
    
    """
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    cargo= models.CharField(max_length=50)
    fecha_ingreso= models.DateField(null=True, blank=True)
    
    """