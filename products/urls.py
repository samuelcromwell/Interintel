from django.urls import path
from .views import ProductBulkCreateAPIView

urlpatterns = [
    path('products/bulk-create/', ProductBulkCreateAPIView.as_view(), name='bulk-create-products'),
]
