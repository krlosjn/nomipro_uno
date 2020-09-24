from django import forms
from apps.administrar_nomina.models import Nomina,Periodo
from apps.gestion_empleado.models import Cargos


class PeriodoForm(forms.ModelForm):
    class Meta:
        model= Periodo

        fields = [
            'ide_periodo',
            'anual',
            'mes',
        ]
        labels = {
            'ide_periodo':'id periodo',
            'anual':'Anual',
            'mes':'Mes'
        
        }
        widgets = {
            'ide_periodo':forms.TextInput(attrs={'class':'form-control'}),
            'anual':forms.TextInput(attrs={'class':'form-control'}),  
            'mes':forms.TextInput(attrs={'class':'form-control'}),       
        }       

class NominaForm(forms.ModelForm):
    class Meta:
        model= Nomina

        fields=[
            'ide_nomina',
            'valorapagar',
            'subtotal',
            'ide_periodo',
            'ide_empleado',    
            'estado',
            'total',
        ]
        labels= {
            'ide_nomina':'ide nomina',            
            'ide_periodo':'id periodo',
            'ide_empleado':'id empleado',            
            'estado':'Estado',
            'valorapagar':'valor a pagar',
            'subtotal':'Subtotal',
            'total':'Total',
        }
        widgets={
            'ide_nomina': forms.TextInput(attrs={'class':'form-control'}),            
            'ide_periodo': forms.TextInput(attrs={'class':'form-control'}),
            'ide_empleado': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            #'valorapagar': forms.ModelMultipleChoiceField(queryset=Cargos.objects.all(),required=True,widget=filter("valorpagar",iterable=False)),
            'valorapagar': forms.Select(attrs={'class':'form-control', 'name': 'id_valorpagar', 'id':'id_valorpagar'}),
            'subtotal': forms.NumberInput(attrs={'class':'form-control'}), 
            'total': forms.NumberInput(attrs={'class':'form-control'}),               
        }       


