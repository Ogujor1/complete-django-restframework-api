from . import views
from django.urls import path

urlpatterns = [
    path('', views.SearchListView.as_view(), name='search'),
]