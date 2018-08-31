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
from Main.views import *

urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    
    url(r'^profile/$', profile, name="profile"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vector/', include("VectorLayers.urls")),
    url(r'^series/', include("TimeSeries.urls")),
    url(r'^raster/', include("RasterLayers.urls")),
    url(r'^tms/', include("tms.urls")),
    url(r'^search/',include("search.urls")),
]
