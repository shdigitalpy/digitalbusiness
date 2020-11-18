from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    'static': StaticViewSitemap,
}

#Attention put every url in sitemap

urlpatterns = [
    path('', views.index, name="index"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

