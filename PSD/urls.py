from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^method/', views.method, name='method'),
    url(r'^result/', views.result, name='result'),
    url(r'^conclusion/', views.conclusion, name='conclusion'),
    url(r'^result/sb1/', views.sub1, name='sub1'),
    url(r'^result/sb2/', views.sub2, name='sub2'),
    url(r'^result/sb3/', views.sub3, name='sub3'),
    url(r'^result/sb4/', views.sub4, name='sub4'),
]