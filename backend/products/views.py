from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.mixins import  StaffEditorPermissionMixin, UserQuerySetMixin
# Create your views here.


class ProductListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView, StaffEditorPermissionMixin):
  """LIST CREATE VIEW"""
  queryset = Product.objects.all()
  serializer_class =  ProductSerializer    
 
 
  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    # email = serializer.validated_data.pop('email')
    # print(email)
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(user=self.request.user, content=content)

  # def get_queryset(self, *args, **kwargs):
  #   qs = super().get_queryset(*args, **kwargs)
  #   request = self.request
  #   user = request.user
  #   #print(request.user)
  #   if not user.is_authenticated:
  #     return Product.objects.none()

  #   return qs.filter(user=request.user)
      


product_list_create_view = ProductListCreateAPIView.as_view()



class ProductMixinView(UserQuerySetMixin, generics.GenericAPIView, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, mixins.CreateModelMixin):
  queryset = Product.objects.all() 
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def get(self, request, *args, **kwargs):
    print(args, kwargs)
    pk = kwargs.get('pk')
    if pk != None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)
  
  def post(self, request, *args, **kwargs):
    return self.create( request, *args, **kwargs)
  
  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = 'I can confirm with this'
    serializer.save(content=content)

product_mixin_view = ProductMixinView.as_view()  

class ProductCreateView(UserQuerySetMixin, generics.CreateAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(content=content)

product_create_view = ProductCreateView.as_view()


class ProductDetailAPIView(UserQuerySetMixin, generics.RetrieveAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  

product_detail_view = ProductDetailAPIView.as_view()  


class ProductUpdateAPIView(UserQuerySetMixin, generics.UpdateAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
 
  

  def perform_update(self, serializer):
    instance = serializer.save()
    if instance.content == None:
      instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()  


class ProductDeleteAPIView(UserQuerySetMixin, generics.DestroyAPIView, StaffEditorPermissionMixin):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  


  def perform_destroy(self, instance):
    super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()  



# Taking Care of all the Views - LIST, DETAIL AND POST using function view

@api_view(["GET", "POST"])
def ProductAltList(request, pk=None, *args, **kwargs):
  if request.method == 'GET':
    if pk != None:
      instance = get_object_or_404(Product, pk=pk)
      if instance:
        data = ProductSerializer(instance, many=False).data
        return Response(data)
      return Response({'invalid':'Bad Request'}, status=400)
  
    else:
      instance = Product.objects.all()
      data = ProductSerializer(instance, many=True).data
      return Response(data)
      
  elif request.method == 'POST':
    data = ProductSerializer(data=request.data)
    if data.is_valid(raise_exception=True):
      instance = data.save()
      return Response(instance.data)
    
  return Response({"invalid":"Bad Request"}, status=404)  



  








  