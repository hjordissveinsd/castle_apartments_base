from django.urls import path


from . import views

urlpatterns = [
    path('',views.browse, name="browse"),
    path('singleEstate', views.singleEstate, name="singleEstate"),
    path('create_estate', views.createEstate, name='create_estate'),
    path('estate_detail', views.clickEstate, name="estate")
]