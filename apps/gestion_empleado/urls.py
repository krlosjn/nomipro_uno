from django.conf.urls import url,include
#from apps.gestion_empleado.views import Cargos_view,Tipo_Vinculacion_view,Empleado_view
from apps.gestion_empleado.views import CargosCreate,index_empleado,CargosList,CargosDelete,CargosUpdate
from apps.gestion_empleado.views import TipoVinculacionCreate,TipoVinculacionList,TipoVinculacionUpdate,TipoVinculacionDelete
from apps.gestion_empleado.views import EmpleadoCreate,EmpleadoList,EmpleadoUpdate
from django.contrib.auth.decorators import login_required
from apps.gestion_empleado.views import CargosDetalles
from apps.gestion_empleado.views import TipoVinculacionDetalles
from apps.gestion_empleado.views import EmpleadoDetalles
from django.urls import path



urlpatterns = [
    
    url(r'^$', index_empleado, name='index empleado'),
    #url(r'^cargos$', Cargos_view, name='cargo crear'),
    url(r'^cargos$', login_required(CargosCreate.as_view()), name='cargos_crear'),
    url(r'^cargoslistar$', login_required(CargosList.as_view()), name='cargos_listar'),
    path('cargosdetalle/<int:pk>', CargosDetalles.as_view(), name='cargos_detalles'),    
    url(r'^cargoseditar/(?P<pk>\d+)/$', login_required(CargosUpdate.as_view()), name='cargos_editar'),
    url(r'^cargoseliminar/(?P<pk>\d+)/$', login_required(CargosDelete.as_view()), name='cargos_eliminar'),
    url(r'^tipovinculacion$', login_required(TipoVinculacionCreate.as_view()), name='tipovinculacion_crear'),
    url(r'^tipovinculacionlistar$', login_required(TipoVinculacionList.as_view()), name='tipovinculacion_listar'),
    path('tipovinculaciondetalle/<int:pk>', login_required(TipoVinculacionDetalles.as_view()), name='tipovinculacion_detalles'), 
    url(r'^tipovinculacioneditar/(?P<pk>\d+)/$',login_required(TipoVinculacionUpdate.as_view()), name='tipovinculacion_editar'),
    url(r'^tipovinculacioneliminar/(?P<pk>\d+)/$',login_required(TipoVinculacionDelete.as_view()), name='tipovinculacion_eliminar'),
    url(r'^empleado$',login_required(EmpleadoCreate.as_view()), name='empleado_crear'),
    url(r'^empleadolistar$',login_required(EmpleadoList.as_view()),name='empleado_listar'),
    path('empleadodetalles/<int:pk>',login_required(EmpleadoDetalles.as_view()),name='empleado_detalles'),
    url(r'^empleadoeditar/(?P<pk>\d+)/$',login_required(EmpleadoUpdate.as_view()), name='empleado_editar'),
]

