from django.shortcuts import render,redirect
from apps.gestion_empleado.forms import CargosForm,TipoVinculacionForm,EmpleadoForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from apps.gestion_empleado.models import Cargos,Tipo_Vinculacion,Empleado
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView

# Create your views here.

def index_empleado(request):
   return render(request,"gestion_empleado/index_empleado.html")
   

# def Cargos_view(request):
#    if request.method == 'POST':
#       form=CargosForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=CargosForm()
#    return render (request,'gestion_empleado/cargos_form.html',{'form':form})

## vamos a crear las diferentes opciones para poder controlar el formulario de cargos
## poder ingresar información, eliminar, actualiza y listar

class CargosList(ListView):
   model=Cargos
   template_name='gestion_empleado/cargos_list.html'

class CargosDetalles(DetailView):
   model=Cargos
   template_name='gestion_empleado/cargos_detalles.html'

class CargosCreate(CreateView):
   model=Cargos
   template_name='gestion_empleado/cargos_form.html'
   form_class=CargosForm
   success_url=reverse_lazy('cargos_listar')
      
class CargosDelete(DeleteView):
   model=Cargos
   template_name='gestion_empleado/cargos_delete.html'
   success_url = reverse_lazy('cargos_listar')

class CargosUpdate(UpdateView):
   model=Cargos
   template_name='gestion_empleado/cargos_form.html'
   form_class=CargosForm
   success_url=reverse_lazy('cargos_listar')

   

## formularios, create,delte,update, list para tipovinculacion
class TipoVinculacionList(ListView):
  model=Tipo_Vinculacion
  template_name='gestion_empleado/tipo_vinculacion_list.html'

class TipoVinculacionDetalles(DetailView):
   model=Tipo_Vinculacion
   template_name='gestion_empleado/tipovinculacion_detalles.html'
   
class TipoVinculacionCreate(CreateView):
   model=Tipo_Vinculacion
   template_name='gestion_empleado/tipo_vinculacion_form.html'
   form_class=TipoVinculacionForm
   success_url=reverse_lazy('tipovinculacion_listar')


class TipoVinculacionUpdate(UpdateView):
   model=Tipo_Vinculacion
   template_name='gestion_empleado/tipo_vinculacion_form.html'
   form_class=TipoVinculacionForm
   success_url=reverse_lazy('tipovinculacion_listar')
   

class TipoVinculacionDelete(DeleteView):
   model=Tipo_Vinculacion
   template_name='gestion_empleado/tipo_vinculacion_delete.html'
   success_url=reverse_lazy('tipovinculacion_listar')
   
   ## vamos a crear el crud para el model de empleado

class EmpleadoCreate(CreateView):
   model=Empleado
   template_name='gestion_empleado/empleado_form.html'
   form_class=EmpleadoForm
   success_url=reverse_lazy('empleado_listar')

class EmpleadoDetalles(DetailView):
   model=Empleado
   template_name='gestion_empleado/empleado_detalles.html'


class EmpleadoList(ListView):
   model=Empleado
   template_name='gestion_empleado/empleado_list.html'

   
class EmpleadoUpdate(UpdateView):
   model=Empleado
   template_name='gestion_empleado/empleado_form.html'
   form_class=EmpleadoForm
   success_url=reverse_lazy('empleado_listar')

   

                   
       
# def Tipo_Vinculacion_view(request):
#    if request.method == 'POST':
#       form=Tipo_VinculacionForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=Tipo_VinculacionForm()
#    return render (request, 'gestion_empleado/tipo_vinculacion_form.html',{'form':form})

# def Empleado_view(request):
#    if request.method == 'POST':
#       form=EmpleadoForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=EmpleadoForm()
#    return render (request, 'gestion_empleado/empleado_form.html',{'form':form}) 