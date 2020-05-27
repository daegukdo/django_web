from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^method/', views.method, name='method'),
    url(r'^result/', views.result, name='result'),
    url(r'^conclusion/', views.conclusion, name='conclusion'),
]