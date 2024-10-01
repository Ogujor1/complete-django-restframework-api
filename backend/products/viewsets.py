from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
  """
    get - list - Queryset
    get - retrieve - product details
    post - add product instance
    patch - Partially Update Product instance
    put - Update product instance
    destroy - Delete product instance
    
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'