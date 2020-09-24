from django.shortcuts import render,redirect
from apps.gestion_tiempo.forms import ParafiscalesForm,DetalleParafiscalForm,Reporte_HorasForm,Horas_AdicionalesForm,Detalle_HorasForm
from django.views.generic import CreateView,ListView,UpdateView
from apps.gestion_tiempo.models import Reporte_Horas,Horas_Adicionales,Parafiscales,DetalleParafiscal,Detalle_Horas
from django.urls import reverse_lazy
from django.views.generic import DetailView


# Create your views here.

def index_tiempo(request):
   return render(request,"gestion_tiempo/index_tiempo.html")

# def Parafiscales_view(request):
#    if request.method == 'POST':
#       form=ParafiscalesForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=ParafiscalesForm()
#    return render (request, 'gestion_tiempo/parafiscales_form.html',{'form':form})

# def Detalle_parafiscal_view(request):
#    if request.method == 'POST':
#       form=DetalleParafiscalForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=DetalleParafiscalForm()
#    return render (request, 'gestion_tiempo/detalleparafiscal_form.html',{'form':form})


# def Reporte_Horas_view(request):
#    if request.method == 'POST':
#       form=Reporte_HorasForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=Reporte_HorasForm()
#    return render (request, 'gestion_tiempo/reportehoras_form.html',{'form':form})

# def Horas_Adicionales_view(request):
#    if request.method == 'POST':
#       form=Horas_AdicionalesForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=Horas_AdicionalesForm()
#    return render (request, 'gestion_tiempo/horasadicionales_form.html',{'form':form})

# def Detalle_Horas_view(request):
#    if request.method == 'POST':
#       form=Detalle_HorasForm(request.POST)
#       if form.is_valid():
#          form.save()
#       return redirect('index')
#    else:
#       form=Detalle_HorasForm()
#    return render (request, 'gestion_tiempo/detallehoras_form.html',{'form':form})


class ReporteHorasCreate(CreateView):
   model=Reporte_Horas
   template_name='gestion_tiempo/reportehoras_form.html'
   form_class=Reporte_HorasForm
   success_url=reverse_lazy('reportehoras_listar')

class ReporteHorasList(ListView):
   model=Reporte_Horas
   template_name='gestion_tiempo/reportehoras_list.html'

class ReporteHorasDetalles(DetailView):
   model=Reporte_Horas
   template_name='gestion_tiempo/reportehoras_detalles.html'

class ReporteHorasUpdate(UpdateView):
   model=Reporte_Horas
   template_name='gestion_tiempo/reportehoras_form.html'
   form_class=Reporte_HorasForm
   success_url=reverse_lazy('reportehoras_listar')

class HorasAdicionalesCreate(CreateView):
   model=Horas_Adicionales
   template_name='gestion_tiempo/horasadicionales_form.html'
   form_class=Horas_AdicionalesForm
   success_url=reverse_lazy('horasadicionales_listar')

class HorasAdcionalesDetalles(DetailView):
   model=Horas_Adicionales
   template_name='gestion_tiempo/horasadicionales_detalles.html'

class HorasAdicionalesList(ListView):
   model=Horas_Adicionales
   template_name='gestion_tiempo/horasadicionales_list.html'

class HorasAdicionalesUpdate(UpdateView):
   model=Horas_Adicionales
   form_class=Horas_AdicionalesForm
   template_name='gestion_tiempo/horasadicionales_form.html'
   success_url=reverse_lazy('horasadicionales_listar')

class ParafiscalesCreate(CreateView):
   model=Parafiscales
   form_class=ParafiscalesForm
   template_name='gestion_tiempo/parafiscales_form.html'
   success_url=reverse_lazy('parafiscales_listar')

class ParafiscalesUpdate(UpdateView):
   model=Parafiscales
   form_class=ParafiscalesForm
   template_name='gestion_tiempo/parafiscales_form.html'
   success_url=reverse_lazy('parafiscales_listar')

class ParafiscalesDetalles(DetailView):
   model=Parafiscales
   template_name='gestion_tiempo/parafiscales_detalles.html'

class ParafiscalesList(ListView):
   model=Parafiscales
   template_name='gestion_tiempo/parafiscales_list.html'

class DetalleParafiscalCreate(CreateView):
   model=DetalleParafiscal
   form_class=DetalleParafiscalForm
   template_name='gestion_tiempo/detalleparafiscal_form.html'
   success_url=reverse_lazy('detalleparafiscal_listar')

class DetalleParafiscalList(ListView):
   model=DetalleParafiscal
   templeate_name='gestion_tiempo/detalleparafiscal_list.html'

class DetalleParafiscalUpdate(UpdateView):
   model=DetalleParafiscal
   form_class=DetalleParafiscalForm
   template_name='gestion_tiempo/detalleparafiscal_form.html'
   success_url=reverse_lazy('detalleparafiscal_listar')

class DetalleParafiscalDetalle(DetailView):
   model=DetalleParafiscal
   template_name='gestion_tiempo/detalleparafiscal_detalle.html'

class DetalleHorasCreate(CreateView):
   model=Detalle_Horas
   form_class=Detalle_HorasForm
   template_name='gestion_tiempo/detallehoras_form.html'
   success_url=reverse_lazy('detallehoras_listar')

class DetalleHorasDetalles(DetailView):
   model=Detalle_Horas
   template_name='gestion_tiempo/detallehoras_detalles.html'

class DetalleHorasUpdate(UpdateView):
   model=Detalle_Horas
   form_class=Detalle_HorasForm
   template_name='gestion_tiempo/detallehoras_form.html'
   success_url=reverse_lazy('detallehoras_listar')

class DetalleHorasList(ListView):
   model=Detalle_Horas
   template_name='gestion_tiempo/detallehoras_list.html'



