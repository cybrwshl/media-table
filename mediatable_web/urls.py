from django.conf.urls import patterns, url

from mediatable_web import views


urlpatterns = patterns('', url(r'^$', views.index, name='index'), )