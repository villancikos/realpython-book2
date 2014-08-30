from django.conf.urls import patterns, include, url
from hello_world import views

urlpatterns = patterns('hello_world.views',
    url(r'^$', views.index, name='index'),
    url(r'^better/$', views.better, name='better'),
    url(r'^about/$', views.about, name='about'),
)
