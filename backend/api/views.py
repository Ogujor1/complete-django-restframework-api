from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer



# Create your views here.
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#   """ DRF VIEWS """
#   instance = Product.objects.all().order_by("?").first()
#   if instance:
#     data = ProductSerializer(instance).data
#   return Response(data)  
  
@api_view(["POST"])
def api_home(request, *args, **kwargs):
  """ DRF VIEWS """
  serializer =  ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data)  
  return Response({'invalid':'not good data'}, status=404)

  