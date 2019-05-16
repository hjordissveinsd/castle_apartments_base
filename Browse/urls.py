from django.urls import path


from . import views

urlpatterns = [
    path('', views.browse, name="estate"),
    path('name', views.order_name, name="filter"),
    path('price_low', views.order_price_low, name="filter2"),
    path('price_high', views.order_price_high, name="filter3"),
    path('singleEstate', views.singleEstate, name="singleEstate"),
    #path('create_estate', views.createEstate, name='create_estate'),
    path('<int:id>/', views.get_estate_by_id, name="estate_detail"),
    path('<int:id>/payment_details', views.payment_details, name='payment_details'),
    path('<int:id>/payment_details/checkout', views.checkout, name='checkout')
]