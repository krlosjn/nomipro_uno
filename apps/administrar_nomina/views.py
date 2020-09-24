from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.administrar_nomina.forms import NominaForm,PeriodoForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from apps.administrar_nomina.models import Periodo,Nomina
from apps.gestion_empleado.models import Empleado, Cargos
from django.urls import reverse_lazy
from django.views.generic import DetailView

# importamos el formulario de parafiscales, Detalle horas, horas adicionales 
# para poder asociar los campos en la nómina
from apps.gestion_tiempo.forms import ParafiscalesForm, Detalle_HorasForm,Horas_AdicionalesForm

from apps.gestion_tiempo.models import Parafiscales,Detalle_Horas,Horas_Adicionales, DetalleParafiscal


# vamos a importar la clase empleado para poder crear una clase index y poder mostrar al inicio los empleados
# registrados

from apps.gestion_empleado.models import Empleado


# Create your views here.
# def index(request): 
#    return render(request,"administrar_nomina/index.html")


class index(ListView):
   model=Empleado   
   template_name='administrar_nomina/index.html'

# def Periodo_view(request):
#    if request.method == 'POST':
#       form=PeriodoForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=PeriodoForm()
#    return render (request, 'administrar_nomina/periodo_form.html',{'form':f

class PeriodoCreate(CreateView):
   model=Periodo
   form_class=PeriodoForm
   template_name='administrar_nomina/periodo_form.html'
   success_url=reverse_lazy('periodo_listar')

class PeriodoList(ListView):
   model=Periodo
   template_name='administar_nomina/periodo_list.html'

class PeriodoDetalles(DetailView):
   model=Periodo
   template_name='administrar_nomina/periodo_detalles.html'

class PeriodoUpdate(UpdateView):
   model=Periodo
   form_class=PeriodoForm
   template_name='administrar_nomina/periodo_form.html'
   success_url=reverse_lazy('periodo_listar')
   

class NominaCreate(CreateView):
   model=Nomina
   template_name='administrar_nomina/nomina_form.html'
   context_object_name='obj'
   form_class = NominaForm
   success_url=reverse_lazy('nomina_listar')

   def get_context_data(self,**kwargs):
      context = super(NominaCreate,self).get_context_data(**kwargs)
      context['form2'] = DetalleParafiscal.objects.all()
      context['form3'] = Detalle_Horas.objects.all()
      context['form4'] = Parafiscales.objects.all()
      context['form5'] = Horas_Adicionales.objects.all()
      context['form6'] = Cargos.objects.all()
      if 'form' not in context:
         context['form'] = self.form_class(self.request.GET)

      return context

   def post(self, request, *args, **kwargs):
      self.object = self.get_object
      form = self.form_class(request.POST)

      if request.method=='POST':
         if form.is_valid():
            Nomina = form.save(commit=False)
            # Nomina.ide_nomina = request.POST.get("id_nomina")           
            # Nomina.ide_periodo = request.POST.get("id_periodo")
            # Nomina.ide_empleado = request.POST.get("id_empleado")
            # Nomina.estado = request.POST.get("id_estado")
            Nomina.valorapagar = request.POST.get("id_valorpagar2")
            Nomina.subtotal = request.POST.get("id_subtotal")
            Nomina.total = request.POST.get("id_total")
            Nomina = form.save()           
            Nomina.save()            
            return HttpResponseRedirect(self.get_success_url())
         else:
            return self.render_to_response(self.get_context_data(form=form))

# necesitamos asociar en las vistas de crear los datos que ingresamos en el formulario para hacer los cálculos, 
# para poder guardarlos


class NominaList(ListView):
   model=Nomina
   context_object_name='obj'
   template_name='administrar_nomina/nomina_list.html'

class NominaDetalles(DetailView):
   model=Nomina
   context_object_name='obj'
   template_name='administrar_nomina/nomina_detalles.html   '

class NominaUpdate(UpdateView):
   model=Nomina
   template_name='administrar_nomina/nomina_form.html'
   context_object_name='obj'
   form_class=NominaForm
   success_url=reverse_lazy('nomina_listar')



# def Nomina_view(request):
#    if request.method == 'POST':
#       form=NominaForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=NominaForm()
#    return render (request, 'administrar_nomina/nomina_form.html',{'form':form})

