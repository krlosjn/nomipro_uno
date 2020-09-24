from django.conf.urls import url,include
from apps.administrar_nomina.views import index
from apps.administrar_nomina.views import PeriodoCreate,PeriodoList,PeriodoUpdate
from apps.administrar_nomina.views import NominaCreate,NominaList,NominaUpdate
from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.administrar_nomina.views import PeriodoDetalles
from apps.administrar_nomina.views import NominaDetalles

urlpatterns = [
    # vamos a colocar para que el inicio sea con la tabla de empleado listar, para esto modificamos el index, con datos
    # correspondiente a los datos del empleado 
    url(r'^$',index.as_view(), name='inicio_listar'),
    #url(r'^nomina$', Nomina_view, name='nomina crear'),
    #url(r'^periodo$', Periodo_view, name='periodo crear'),
    url(r'^periodo/$',login_required(PeriodoCreate.as_view()), name='periodo_crear'),
    url(r'^periodolistar/$',login_required(PeriodoList.as_view()), name='periodo_listar'),
    path('periododetalles/<int:pk>',login_required(PeriodoDetalles.as_view()), name='periodo_detalles'),
    url(r'^periodoeditar/(?P<pk>\d+)/$',login_required(PeriodoUpdate.as_view()), name='periodo_editar'),
    url(r'^nomina/$', login_required(NominaCreate.as_view()), name="nomina_crear"),
    url(r'^nominalistar/$', login_required(NominaList.as_view()), name="nomina_listar"),
    path('nominadetalles/<int:pk>', login_required(NominaDetalles.as_view()), name='nomina_detalles'),
    url(r'^nominaeditar/(?P<pk>\d+)/$',login_required(NominaUpdate.as_view()), name='nomina_editar'),  
]
