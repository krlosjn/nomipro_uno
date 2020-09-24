from django.db import models
from apps.gestion_empleado.models import Empleado

# Create your models here 

nomina_estado = [
    (1, 'activo'),
    (2, 'inactivo')
]


class Periodo(models.Model):
    ide_periodo=models.AutoField(primary_key=True)
    anual=models.CharField(max_length=50)
    mes=models.CharField(max_length=50)

    #def __str__(self):
        #return '{} {} {}'.format(self.ide_periodo, self.anual, self.mes)

class Nomina(models.Model):
    ide_nomina=models.AutoField(primary_key=True) 
    ide_periodo=models.ForeignKey(Periodo,null=True,blank=True,on_delete=models.CASCADE)
    ide_empleado=models.ForeignKey(Empleado,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.IntegerField(null=True, blank=True, choices = nomina_estado, default=1)
    valorapagar=models.FloatField(null=True, blank=True)#Salario
    subtotal=models.FloatField(null=True, blank=True)#Salario antes de deducciones
    total=models.FloatField(null=True, blank=True)


    #def __str__(self):
        #return'{} {} {} {} {} {}'.format(self.ide_nomina,self.ide_periodo,self.ide_empleado,self.valorapagar,self.subtotal,self.estado,self.total)
        
