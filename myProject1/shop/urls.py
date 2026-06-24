from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('product/', views.product, name='shop-product'),
]