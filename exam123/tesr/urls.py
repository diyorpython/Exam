from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<slug:slug>/', ProductRetirieveUpdateDeleteAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<slug:slug>/', CategoryRetrieveUpdateDeleteAPIView.as_view()),
    path('inventory/', InventoryListCreateAPIView.as_view()),
    path('inventory/<int:pk>', InventoryRetirieveUpdateDeleteAPIView.as_view()),
    path("customer/", CustomerListCreateAPIView.as_view()),
    path("customer/<int:pk>", CustomerRetirieveUpdateDeleteAPIView.as_view()),
    path("order", OrderListCreateAPIView.as_view()),
    path("order/<int:pk>", OrderRetirieveUpdateDeleteAPIView.as_view()),
    path("productphoto/", ProductListCreateAPIView.as_view()),
    path("productphoto/<int:pk>", ProductPhotoRetirieveUpdateDeleteAPIView.as_view())
]