from rest_framework import serializers
from .models import Category, Product, Inventory, Customer, Order, Product_Photo

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name", "desc")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("category", "name", "desc", "price")

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ("product", "stock_status", "quantity")

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("full_name", "email", "phone_number", "adress")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("Customer", "product", "total_proce")

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Photo
        fields = ("product", "thumblin_pc", "large_pc")