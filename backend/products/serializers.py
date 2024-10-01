from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from . import validators 
from api.serializers import UserPublicSerializer

class ProductInLineSerializer(serializers.Serializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
  title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
  owner = UserPublicSerializer(source= 'user', read_only=True)
  body = serializers.CharField(source='content')
  # my_user_data = serializers.SerializerMethodField(read_only=True)
  # related_products = ProductInLineSerializer(source='user.product_set.all', read_only=True, many=True) 
  discount = serializers.SerializerMethodField(read_only=True)
  # edit_url = serializers.SerializerMethodField(read_only=True)
  # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
  title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
  #name = serializers.CharField(source='title', read_only=True)
  #email = serializers.EmailField(source = 'user.email', read_only=True)
  class Meta:
    model = Product
    fields = [
      'owner',
      #'email',
      #'url',  
      #'edit_url', 
      'pk', 'endpoint','title', 'body', 'price', 'sale_price', 'discount', 'public','path',
      # 'my_user_data', 
      # 'related_products'
      ]

  def get_my_user_data(self, obj):
    return {
      'username': obj.user.username
    }  
    

  # def validate_title(self, value):
  #   request = request.context.get('request')
  #   user = request.user
  #   qs = Product.objects.filter(user=user, title__iexact=value)
  #   if qs.exists():
  #     raise serializers.ValidationError(f"{value} is already a product name")
  #   return value
  

  # def create(self, validated_data):
  #   # email = validated_data.pop('email')
  #   return Product.objects.create(**validated_data)
  #   obj = super().create(validated_data)  
  #   # print(email, obj)
  #   return obj
  
  # def update(self, instance, validated_data):
  #   email = validated_data.pop('email')
  #   instance.title = validated_data.get('title')
  #   return super().update(instance, validated_Data)

  def get_edit_url(self, obj):
    #return f"api/products/{obj.pk}/"
    request = self.context.get('request')
    if request is None:
      return None
    return reverse("product-edit", kwargs={'pk':obj.pk}, request=request)


  def get_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    
    if not isinstance(obj, Product):
      return None
    return obj.get_discount() 
