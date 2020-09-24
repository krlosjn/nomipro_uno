from django.conf.urls import url,include
#from apps.gestion_tiempo.views import Detalle_Horas_view,Parafiscales_view,Reporte_Horas_view,Detalle_parafiscal_view,Horas_Adicionales_view,index_tiempo
from apps.gestion_tiempo.views import index_tiempo, ReporteHorasCreate,ReporteHorasList,ReporteHorasUpdate
from apps.gestion_tiempo.views import HorasAdicionalesCreate,HorasAdicionalesList,HorasAdicionalesUpdate
from apps.gestion_tiempo.views import ParafiscalesCreate,ParafiscalesUpdate,ParafiscalesList
from apps.gestion_tiempo.views import DetalleParafiscalCreate,DetalleParafiscalList,DetalleParafiscalUpdate
from apps.gestion_tiempo.views import DetalleHorasCreate,DetalleHorasList,DetalleHorasUpdate
from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.gestion_tiempo.views import DetalleHorasDetalles,ParafiscalesDetalles,DetalleParafiscalDetalle
from apps.gestion_tiempo.views import ReporteHorasDetalles,HorasAdcionalesDetalles

urlpatterns = [
    url(r'^$', index_tiempo, name='index tiempo'),
    #url(r'^detalleparafiscal$', Detalle_parafiscal_view, name='cargo crear'),
    #url(r'^parafiscales$', Parafiscales_view, name='parafiscales crear'),
    #url(r'^reportehoras$', Reporte_Horas_view, name='reporte horas crear'),
    #url(r'^detallehoras$', Detalle_Horas_view, name='detalle horas crear'),
    #url(r'^horasadicionales$', Horas_Adicionales_view, name='horas adicionales crear'),
    url(r'^reportehoras$',login_required(ReporteHorasCreate.as_view()), name='reportehoras_crear'),
    url(r'^reportehoraslistar$',login_required(ReporteHorasList.as_view()),name='reportehoras_listar'),
    url(r'^reportehoraseditar/(?P<pk>\d+)/$',login_required(ReporteHorasUpdate.as_view()),name='reportehoras_editar'),
    path('reportehorasdetalles/<int:pk>', login_required(ReporteHorasDetalles.as_view()), name='reportehoras_detalles'),
    url(r'^horasadicionales$',login_required(HorasAdicionalesCreate.as_view()), name='horasadicionales_crear'),
    url(r'^horasadicionaleslistar$',login_required(HorasAdicionalesList.as_view()), name='horasadicionales_listar'),
    url(r'^horasadicionaleseditar/(?P<pk>\d+)/$',login_required(HorasAdicionalesUpdate.as_view()),name='horasadicionales_editar'),
    path('horasadicionalesdetalles/<int:pk>',login_required(HorasAdcionalesDetalles.as_view()), name='horasadicionales_detalles'),
    url(r'^parafiscales$', login_required(ParafiscalesCreate.as_view()), name='parafiscales_crear' ),
    url(r'^parafiscaleseditar/(?P<pk>\d+)/$',login_required(ParafiscalesUpdate.as_view()),name='parafiscales_editar'),
    url(r'^parafiscaleslistar$', login_required(ParafiscalesList.as_view()),name='parafiscales_listar'),
    path('parafiscalesdetalles/<int:pk>',login_required(ParafiscalesDetalles.as_view()), name='parafiscales_detalles'),
    url(r'^detalleparafiscal$', login_required(DetalleParafiscalCreate.as_view()),name='detalleparafiscal_crear'),
    url(r'^detalleparafiscallistar$', login_required(DetalleParafiscalList.as_view()), name='detalleparafiscal_listar'),
    path('detalleparafiscaldetalles/<int:pk>',login_required(DetalleParafiscalDetalle.as_view()), name='detalleparafiscal_detalles'),
    url(r'^detalleparafiscaleditar/(?P<pk>\d+)/$',login_required(DetalleParafiscalUpdate.as_view()),name='detalleparafiscal_editar'),
    url(r'^detallehoras$',login_required(DetalleHorasCreate.as_view()), name='detallehoras_crear'),
    url(r'^detallehoraslistar$',login_required(DetalleHorasList.as_view()), name='detallehoras_listar'),
    path('detallehorasdetalles/<int:pk>',login_required(DetalleHorasDetalles.as_view()), name='detallehoras_detalles'),
    url(r'^detallehoraseditar/(?P<pk>\d+)/$',login_required(DetalleHorasUpdate.as_view()),name='detallehoras_editar'),
    
     
]
