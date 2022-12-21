from django import forms

class ColaboradorForm(forms.Form):
    nombre= forms.CharField(label="Nombre:",max_length=50)
    apellido= forms.CharField(label="Apellido:",max_length=50)
    dni= forms.IntegerField(label="DNI:",)
    cargo= forms.CharField(label="cargo:",max_length=50)
    fecha_ingreso= forms.DateField(label="Fecha de ingreso:")

    
    """
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    dni= models.IntegerField()
    cargo= models.CharField(max_length=50)
    fecha_ingreso= models.DateField(null=True, blank=True)
    
    """