
from django.urls import path
from . import views
from .views import order_history


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('order_history/', order_history, name='order_history'),
    
    
]