from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    # path('',views.create_sale(), name="create_sale")
    path('', views.sell, name="sell"),
    path('put_up', views.put_up, name='put_up')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)