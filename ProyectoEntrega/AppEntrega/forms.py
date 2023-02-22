from django import forms

class EstiloFormulario(forms.Form):
    estilo= forms.CharField()

class MagoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()

class TrucoFormulario(forms.Form):
    nombre= forms.CharField() 
    clase= forms.CharField()

class BusquedaMago(forms.Form):
    nombre =  forms.CharField()