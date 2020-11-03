from django import forms 
from django.contrib import admin
from .models import Producto, TiposProducto, Proveedor, Rubros

class ProductoAdmin(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['id_producto']
        widgets ={
            'nombre':forms.TextInput(attrs={'id':'nombre','class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'id':'descripcion','class':'form-control'}),
            'p_compra':forms.TextInput(attrs={'id':'p_compra','class':'form-control'}),
            'p_venta':forms.TextInput(attrs={'id':'p_venta','class':'form-control'}),
            'stock':forms.NumberInput(attrs={'id':'stock','class':'form-control'}),
            'fecha_venc':forms.DateTimeInput(attrs={'id':'fecha_venc','class':'form-control'}),
            'id_familia':forms.Select(choices=TiposProducto,attrs={'id':'categoria','class':'form-control'}),
            'id_proveedor':forms.Select(choices=TiposProducto,attrs={'id':'proveedor','class':'form-control'}),
            'id_ref':forms.NumberInput(attrs={'id':'ref','class':'form-control'})
        }
        labels={
            'id_familia':'categoria producto',
            'id_proveedor':'provedoor',
            'p_compra':'precio de compra',
            'p_venta':'precio de venta'
        }

class ProveedorAdmin(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude =['direccion']
        widgets = {
            'rut':forms.TextInput(attrs={'id':'rut','class':'form-control','value':''}),
            'nombre':forms.TextInput(attrs={'id':'nombre','class':'form-control'}),
            'apellido':forms.TextInput(attrs={'id':'apellido','class':'form-control'}),
            'telefono':forms.TextInput(attrs={'id':'telefono','class':'form-control'}),
            'tipo':forms.TextInput(attrs={'id':'tipo','class':'form-control','readonly':''}),
            'rubro':forms.CheckboxSelectMultiple(choices=TiposProducto)
        }
        

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'id': 'username','class':'form-control','placeholder':'Ingrese su nombre de usuario'}))
    password = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'id':'password','class':'form-control','placeholder':'Ingrese su contraseña'}))
