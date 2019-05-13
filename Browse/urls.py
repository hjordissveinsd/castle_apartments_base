from django.urls import path


from . import views

urlpatterns = [
    path('',views.browse, name="estate"),
    path('singleEstate', views.singleEstate, name="singleEstate"),
    path('create_estate', views.createEstate, name='create_estate'),
    path('<int:id>', views.get_estate_by_id, name="estate_detail"),
    #raggi að búa til kaup checkout
    path('checkout', views.checkout, name="checkout")
]