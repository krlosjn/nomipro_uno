from django import forms
from apps.gestion_tiempo.models import Parafiscales,DetalleParafiscal,Detalle_Horas,Reporte_Horas,Horas_Adicionales



class ParafiscalesForm(forms.ModelForm):
    class Meta:
        model= Parafiscales

        fields = [
            'ide_parafiscales',
            'nombre',
            'valor',
            'estado',
            'ide_tipovinculacion',
            

        ]
        labels = {
            'ide_parafiscales':'id parafiscales',
            'nombre':'Nombre',
            'valor':'Valor',
            'estado':'Estado',
            'ide_tipovinculacion':'id tipovinculacion',
            
            
        }
        widgets = {
            'ide_parafiscales':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(attrs={'class':'form-control'}),
            'ide_tipovinculacion':forms.TextInput(attrs={'class':'form-control'}),
           
        }


class DetalleParafiscalForm(forms.ModelForm):
    class Meta:
        model= DetalleParafiscal

        fields = [
            'ide_detalleparafiscal',
            'ide_nomina',
            'totalparafiscal',
            'ide_parafiscales',
           
        ]
        labels = {
            'ide_detalleparafiscal':'id detalleparafiscal',
            'ide_nomina':'id nomina',
            'totalparafiscal':'total parafiscal',
            'ide_parafiscales':'id parafiscales',


        }
        widgets = {
            'ide_detalleparafiscal': forms.TextInput(attrs={'class':'form-control'}),
            'ide_nomina': forms.TextInput(attrs={'class':'form-control'}),
            'totalparafiscal': forms.TextInput(attrs={'class':'form-control'}),
            'ide_parafiscales': forms.TextInput(attrs={'class':'form-control'}),
        
        }       


class Reporte_HorasForm(forms.ModelForm):
    class Meta:
        model= Reporte_Horas

        fields = [
            'ide_reportehoras',
            'ide_empleado',
            'ide_periodo',
            'numerohoras',
           
        ]
        labels = {
            'ide_reportehoras':'id reporte horas',
            'ide_empleado':'id empleado',
            'ide_periodo':'id periodo',
            'numerohoras':'numero horas',
           

        }
        widgets = {
            'ide_reportehoras': forms.TextInput(attrs={'class':'form-control'}),
            'ide_empleado': forms.TextInput(attrs={'class':'form-control'}),
            'ide_periodo': forms.TextInput(attrs={'class':'form-control'}),
            'numerohoras': forms.TextInput(attrs={'class':'form-control'}),
        
        }    


class Horas_AdicionalesForm(forms.ModelForm):
    class Meta:
        model= Horas_Adicionales

        fields = [
            'ide_horasadicionales',
            'nombre',
            'valor_porhora',
            'estado',
            
           
        ]
        labels = {
            'ide_horasadicionales':'id horas adicionales',
            'nombre':'Nombre',
            'valor_porhora':'Valor por hora',
            'estado':'Estado',
            
           

        }
        widgets = {
            'ide_horasadicionales': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'valor_porhora': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            
        
        }       

class Detalle_HorasForm(forms.ModelForm):
    class Meta:
        model= Detalle_Horas

        fields = [
            'ide_detallehoras',
            'ide_nomina',
            'ide_horasadicionales',
            'total',
            'cantidad',
           
        ]
        labels = {
           'ide_detallehoras':'id detalle horas',
           'ide_nomina':'id nomina',
           'ide_horasadicionales':'id horas adicionales',
           'total':'Total',
           'cantidad':'Cantidad',
           
        }
        widgets = {
            'ide_detallehoras': forms.TextInput(attrs={'class':'form-control'}),
            'ide_nomina': forms.TextInput(attrs={'class':'form-control'}),
            'ide_horasadicionales': forms.TextInput(attrs={'class':'form-control'}),
            'total': forms.TextInput(attrs={'class':'form-control'}),
            'cantidad':forms.TextInput(attrs={'class':'form-control'}),  
        }  

        