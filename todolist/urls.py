from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns =  [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]
