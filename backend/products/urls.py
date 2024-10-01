from django.urls import path
from .views import product_detail_view, product_create_view, product_list_create_view, product_update_view, ProductAltList, product_delete_view, product_mixin_view

urlpatterns = [
  path('', product_list_create_view, name='product-list'),
  path('<int:pk>/update', product_update_view, name='product-edit'),
  path('<int:pk>/delete', product_delete_view),
  path('list-create/', product_list_create_view),
  # path('', ProductAltList,),
  path('<int:pk>/',product_detail_view, name='product-detail'),
]
