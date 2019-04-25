"""RESCLIMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from main.views import *
from django.contrib.auth.views import logout
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .api import router
from main import logistica, censo, clima
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
	url(r'^$', home, name="home"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
	url(r'^noAccess/$', noAccess, name="noAccess"),
	url(r'^get-task-info/',get_task_info,name="taskInfo"),
    url(r'^api/', include(router.urls)),
    url(r'^celery-progress/', include('celery_progress.urls')),
	url(r'^profile/$', profile, name="profile"),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/',include("search.urls")),
	url(r'^layer/',include("layer.urls")),
	url(r'^vector/', include("vectorLayers.urls")),
	url(r'^series/', include("timeSeries.urls")),
	url(r'^raster/', include("rasterLayers.urls")),
	url(r'^tms/', include("tms.urls")),
	url(r'^help/$', helpfaq, name='help'),
    url(r'^help/jsonquestion/$', jsonfaqs, name='jsonquestion' ),
	url(r'^dashboards/$', products, name='products'),
    url(r'^simulation/', include("simulation.urls")),
    url(r'^plot/', include('d3.urls')),
    url(r'^dashboard/', include('dash.urls')),
    url(r'^dashboard/', include('dash.contrib.apps.public_dashboard.urls')),
	    ################################ LOGISTICA #################################
    url(r'^data/create/$', logistica.LogisticaCreate, name='logistica_create'),
    url(r'^data/$', login_required(logistica.LogisticaList.as_view(), login_url='noAccess'), name='logistica_list'),
    url(r'^data/update/(?P<pk>\d+)/$', login_required(logistica.LogisticaUpdate.as_view(), login_url='noAccess'), name='logistica_update'),
    url(r'^data/delete/(?P<pk>\d+)/$', login_required(logistica.LogisticaDelete.as_view(), login_url='noAccess'), name='logistica_delete'),
    url(r'^data/show/(?P<pk>\d+)/$', login_required(logistica.LogisticaShow.as_view(), login_url='noAccess'), name='logistica_show'),
    ################################ CLIMA #################################
    url(r'^clima/create/$', clima.ClimaCreate, name='clima_create'),
    url(r'^clima/$', login_required(clima.ClimaList.as_view(), login_url='noAccess'), name='clima_list'),
    url(r'^clima/update/(?P<pk>\d+)/$', login_required(clima.ClimaUpdate.as_view(), login_url='noAccess'), name='clima_update'),
    url(r'^clima/delete/(?P<pk>\d+)/$', login_required(clima.ClimaDelete.as_view(), login_url='noAccess'), name='clima_delete'),
    url(r'^clima/show/(?P<pk>\d+)/$', login_required(clima.ClimaShow.as_view(), login_url='noAccess'), name='clima_show'),
    ################################ CENSO #################################
    url(r'^censo/create/$', censo.CensoCreate, name='censo_create'),
    url(r'^censo/$', login_required(censo.CensoList.as_view(), login_url='noAccess'), name='censo_list'),
    url(r'^censo/update/(?P<pk>\d+)/$', login_required(censo.CensoUpdate.as_view(), login_url='noAccess'), name='censo_update'),
    url(r'^censo/delete/(?P<pk>\d+)/$', login_required(censo.CensoDelete.as_view(), login_url='noAccess'), name='censo_delete'),
    url(r'^censo/show/(?P<pk>\d+)/$', login_required(censo.CensoShow.as_view(), login_url='noAccess'), name='censo_show'),
]

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
