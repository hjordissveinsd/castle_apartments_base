from django.urls import path

from . import views

urlpatterns = [
    #path('',views.create_sale(), name="create_sale")
    path('',views.sell, name="sell")
]