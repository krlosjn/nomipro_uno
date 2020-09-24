from django import forms
from apps.gestion_empleado.models import Empleado,Tipo_Vinculacion,Cargos


class CargosForm(forms.ModelForm):
    class Meta:
        model= Cargos

        fields = [
            'ide_cargos',
            'nombre',
            'estado',
            'valor_cargo',

        ]
        labels = {
            'ide_cargos':'id_cargos',
            'nombre':'Nombre',
            'estado':'Estado',
            'valor_cargo':'valor por cargo',
        }
        widgets = {
            'ide_cargos':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'valor_cargo':forms.TextInput(attrs={'class':'form-control'}),
        }

class TipoVinculacionForm(forms.ModelForm):
    class Meta:
        model= Tipo_Vinculacion

        fields = [
            'ide_tipovinculacion',
            'descripciontipo',
            'estado',
            

        ]
        labels = {
            'ide_tipovinculacion':'id_tipovinculacion',
            'descripciontipo':'Descripciontipo',
            'estado':'Estado',
            
        }
        widgets = {
            'ide_tipovinculacion':forms.TextInput(attrs={'class':'form-control'}),
            'descripciontipo':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),

        }

        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model= Empleado

        fields = [
            'ide_empleado',
            'nombre',
            'apellido',
            'correo',
            'telefono',
            'numero_documento',
            'tipo_documento',
            'ide_cargos',
            'ide_tipovinculacion',
            'estado',            

        ]
        labels = {
            'ide_empleado':'id_empleado',
            'nombre':'Nombre',
            'apellido':'Apellido',
            'correo':'Correo',
            'telefono':'Telefono',
            'numero_documento':'Numero documento',
            'tipo_documento':'Tipo documento',
            'ide_cargos':'id cargos',
            'ide_tipovinculacion':'id tipovinculación',
            'estado': 'Estado',
            
            
        }
        widgets = {
           
            'ide_empleado':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.TextInput(attrs={'class':'form-control'}),
            'telefono':forms.TextInput(attrs={'class':'form-control'}),
            'numero_documento':forms.TextInput(attrs={'class':'form-control'}),
            'tipo_documento':forms.TextInput(attrs={'class':'form-control'}),
            'ide_cargos':forms.TextInput(attrs={'class':'form-control'}),
            'ide_tipovinculacion':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
             
        }