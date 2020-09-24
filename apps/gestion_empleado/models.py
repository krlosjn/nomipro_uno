from django.db import models

# Create your models here.


cargos_estado= [
    (1,'Activo'),
    (2,'Inactivo')
]

tipovinculacion_estado= [
    (1,'Activo'),
    (2,'Inactivo')
]

empleado_estado = [
    (1,'Activo'),
    (2,'Inactivo')
]



class Cargos(models.Model):
    ide_cargos=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50) 
    estado=models.IntegerField(null=False, blank=False, choices = cargos_estado, default=1)
    valor_cargo=models.FloatField()    

    def __str__(self):
        return '{} {} {} {}'.format(self.ide_cargos,self.nombre,self.estado,self.valor_cargo)
        

class Tipo_Vinculacion(models.Model):
    
    ide_tipovinculacion=models.CharField(max_length=50,primary_key=True)
    descripciontipo=models.CharField(max_length=50)
    estado=models.IntegerField(null=False, blank=False, choices = tipovinculacion_estado, default=1)

    def __str__(self):
        return '{} {} {}'.format(self.ide_tipovinculacion,self.descripciontipo,self.estado)

class Empleado(models.Model):
    ide_empleado=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correo=models.EmailField()
    telefono=models.CharField(max_length=20)
    numero_documento=models.CharField(max_length=50)
    tipo_documento=models.CharField(max_length=50)
    ide_cargos=models.ForeignKey(Cargos,null=True,blank=True,on_delete=models.CASCADE)
    ide_tipovinculacion=models.ForeignKey(Tipo_Vinculacion,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.IntegerField(null=False, blank=False, choices = empleado_estado, default=1)
    # me muestra la fecha de cuando creo un empleado;
    created_empleado=models.DateTimeField(auto_now_add=True)
    # me actualiza la fecha de cuando creo un empleado
    update_empleado=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.ide_empleado,self.nombre,self.apellido,self.correo,self.telefono,self.numero_documento,self.tipo_documento,self.ide_cargos,self.ide_tipovinculacion,self.estado,self.created_empleado)