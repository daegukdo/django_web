from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analysis/', views.analysis, name='analysis'),
    path('map/', views.map, name='map'),
    path('summary/', views.summary, name='summary'),
]