from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from rest_framework.response import Response
from products.serializers import ProductSerializer
from . import client


class SearchListView(generics.GenericAPIView):
  def get(self, request, *args, **kwargs):
    user = request.user
    username = None
    if user.is_authenticated:
      user = user.username
    else:
      user = None  
    query = request.GET.get('q')
    public = str(request.GET.get('public')) != '0'
    tag = request.GET.get('tag') or None
    if not query:
      return Response("{detail : Query parameter is required}", status=400)
    result = client.perform_search(query, tags=tag, user=user, public=public )
    return Response(result)


# class SearchListView(generics.GenericAPIView):

#     def get(self, request, *args, **kwargs):
#         user = request.user  # Set the user to request.user object
#         username = None      # Initialize username as None

#         # Check if the user is authenticated
#         if user.is_authenticated:
#             username = user.username  # Assign the username if authenticated

#         # Get search parameters
#         query = request.GET.get('q')
#         public = str(request.GET.get('public')) != '0'
#         tag = request.GET.get('tag') or None

#         # Check if query is provided
#         if not query:
#             return Response({"detail": "Query parameter is required."}, status=400)

#         # Perform search
#         result = client.perform_search(query, tags=tag, user=username, public=public)

#         return Response(result)


class SearchListOldView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def get_queryset(self, *args, **kwargs):
    qs  = super().get_queryset(*args, **kwargs)
    q = self.request.GET.get('q')
    results = Product.objects.none()
    if q is not None:
      user = None
      if self.request.user.is_authenticated:
        user = self.request.user
      results = qs.search(q, user=user)
    return results
  
  

