from django.urls import path
from .views import ProductBulkCreateAPIView
from . import views


urlpatterns = [
    path('products/bulk-create/', ProductBulkCreateAPIView.as_view(), name='bulk-create-products'),
    path('products/', views.get_products, name='get_products'),
]
