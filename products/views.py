from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

class ProductBulkCreateAPIView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Products and variants created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        # Retrieve all products from the database
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)  # Serialize the products along with their variants
        return Response(serializer.data)
