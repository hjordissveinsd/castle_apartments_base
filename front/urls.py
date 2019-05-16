from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main-front'),
    path('about-us', views.aboutUs, name="aboutUs"),
    path('teenage', views.teenage, name="teenage"),
    path('texas', views.texas, name="texas"),
    #path('front/', views.index, name='front')
    ]
