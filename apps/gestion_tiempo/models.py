from django.db import models
from apps.gestion_empleado.models import Empleado,Tipo_Vinculacion
from apps.administrar_nomina.models import Periodo
from apps.administrar_nomina.models import Nomina

# Create your models here.

horas_adicionales_estado= [

    (1,'Activo'),
    (2,'Inactivo')
]

parafiscales_estado= [

    (1,'Activo'),
    (2,'Inactivo')
]


class Reporte_Horas(models.Model):
    ide_reportehoras=models.CharField(max_length=50,primary_key=True)
    ide_empleado=models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE) 
    ide_periodo=models.ForeignKey(Periodo,null=True,blank=True,on_delete=models.CASCADE)
    numerohoras=models.IntegerField() 

 
    def __str__(self):
        return'{} {} {} {}'.format(self.ide_reportehoras,self.ide_empleado,self.ide_periodo,self.numerohoras)


class Horas_Adicionales(models.Model):
    ide_horasadicionales=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    valor_porhora=models.FloatField()
    estado=models.IntegerField(null=False, blank=False, choices = horas_adicionales_estado, default=1)
    ide_reportehoras=models.ForeignKey(Reporte_Horas, null= True,blank=True, on_delete=models.CASCADE)

 
    def __str__(self):
        return'{} {} {} {} {}'.format(self.ide_horasadicionales,self.nombre,self.valor_porhora,self.estado,self.ide_reportehoras)

    
class Parafiscales(models.Model):
    ide_parafiscales=models.CharField(max_length=50,primary_key=True) 
    nombre=models.CharField( max_length=50)
    valor=models.CharField(max_length=50) 
    estado=models.IntegerField(null=False, blank=False, choices = parafiscales_estado, default=1)
    ide_tipovinculacion=models.ForeignKey(Tipo_Vinculacion,null=True,blank=True,on_delete=models.CASCADE)
 
 
    def __str__(self):
        return'{} {} {} {} {}'.format(self.ide_parafiscales,self.nombre,self.valor,self.estado,self.ide_tipovinculacion)

class DetalleParafiscal(models.Model):
        
    ide_detalleparafiscal=models.CharField(max_length=50,primary_key=True)
    ide_nomina=models.ForeignKey(Nomina,null=True,blank=True,on_delete=models.CASCADE)
    totalparafiscal=models.FloatField()
    ide_parafiscales=models.ForeignKey(Parafiscales,null=True,blank=True, on_delete=models.CASCADE)
 
    def __str__(self):
        return'{} {} {} {}'.format(self.ide_detalleparafiscal,self.ide_nomina,self.totalparafiscal,self.ide_detalleparafiscal)

class Detalle_Horas(models.Model):
    ide_detallehoras=models.CharField(max_length=50, primary_key=True) 
    ide_nomina=models.ForeignKey(Nomina,null=True,blank=True,on_delete=models.CASCADE)
    ide_horasadicionales=models.ForeignKey(Horas_Adicionales, null=True,blank=True,on_delete=models.CASCADE)
    total=models.IntegerField()
    cantidad=models.IntegerField()
    
    

 
    def __str__(self):
        return'{} {} {} {} {}'.format(self.ide_detallehoras,self.ide_nomina,self.ide_horasadicionales,self.total,self.cantidad)

