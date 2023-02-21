from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategorySerializer, ProductPhotoSerializer, ProductSerializer, InventorySerializer, CustomerSerializer, OrderSerializer
from .models import Category, Product, Inventory, Customer, Order, Product_Photo

class CategoryListCreateAPIView(APIView):
    serializer_class = CategorySerializer
    def get(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class CategoryRetrieveUpdateDeleteAPIView(APIView):
    serializer_class = CategorySerializer
    def get(self, request, slug):
        categories = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(categories)
        return Response(data=serializer.data)
    
    def put(self, request, slug):
        data = request.data
        categories = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(instance=categories, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def patch(self, request, slug):
        data = request.data
        categories = get_object_or_404(Category, slug=slug)
        serializer = self.serializer_class(instance=categories, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

    def delete(self, request, slug):
        categories = get_object_or_404(Category, slug=slug)
        categories.delete()
        return Response(data={"deleted": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProductListCreateAPIView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer =self.serializer_class(product, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class ProductRetirieveUpdateDeleteAPIView(APIView):
    serializer_class = ProductSerializer
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(product)
        return Response(data=serializer.data)
    
    def put(self, request, slug):
        data= request.data
        product = get_object_or_404(Product, slug=slug)
        serializer =self.serializer_class(instance=product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request, slug):
        data= request.data
        product = get_object_or_404(Product, slug=slug)
        serializer = self.serializer_class(instance=product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return Response(data={"deleted":"product"},status=status.HTTP_204_NO_CONTENT)
    

class InventoryListCreateAPIView(APIView):
    serializer_class = InventorySerializer
    def get(self, request, *args, **kwargs):
        inventory = Inventory.objects.all()
        serializer =self.serializer_class(inventory, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class InventoryRetirieveUpdateDeleteAPIView(APIView):
    serializer_class = InventorySerializer
    def get(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer = self.serializer_class(inventory)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data= request.data
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer =self.serializer_class(instance=inventory, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request, pk):
        data= request.data
        inventory = get_object_or_404(Inventory, pk=pk)
        serializer = self.serializer_class(instance=inventory, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, pk):
        inventory = get_object_or_404(Inventory, pk=pk)
        inventory.delete()
        return Response(data={"deleted":"product"},status=status.HTTP_204_NO_CONTENT)
    


class CustomerListCreateAPIView(APIView):
    serializer_class = Customer
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        serializer =self.serializer_class(customer, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class CustomerRetirieveUpdateDeleteAPIView(APIView):
    serializer_class = CustomerSerializer
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = self.serializer_class(customer)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data= request.data
        customer = get_object_or_404(Customer, pk=pk)
        serializer =self.serializer_class(instance=customer, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request, pk):
        data= request.data
        customer = get_object_or_404(Customer, pk=pk)
        serializer = self.serializer_class(instance=customer, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response(data={"deleted":"product"}, status=status.HTTP_204_NO_CONTENT)
    

class OrderListCreateAPIView(APIView):
    serializer_class = OrderSerializer
    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        serializer =self.serializer_class(order, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class OrderRetirieveUpdateDeleteAPIView(APIView):
    serializer_class = OrderSerializer
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(order)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data= request.data
        order = get_object_or_404(Order, pk=pk)
        serializer =self.serializer_class(instance=order, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request, pk):
        data= request.data
        order = get_object_or_404(Order, pk=pk)
        serializer = self.serializer_class(instance=order, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return Response(data={"deleted":"product"}, status=status.HTTP_204_NO_CONTENT)
    

class ProductPhotoListCreateAPIView(APIView):
    serializer_class = ProductPhotoSerializer
    def get(self, request, *args, **kwargs):
        product_photo = Product_Photo.objects.all()
        serializer =self.serializer_class(product_photo, many=True)
        return Response(data=serializer.data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class ProductPhotoRetirieveUpdateDeleteAPIView(APIView):
    serializer_class = ProductPhotoSerializer
    def get(self, request, pk):
        product_photo = get_object_or_404(Product_Photo, pk=pk)
        serializer = self.serializer_class(product_photo)
        return Response(data=serializer.data)
    
    def put(self, request, pk):
        data= request.data
        product_photo = get_object_or_404(Product_Photo, pk=pk)
        serializer =self.serializer_class(instance=product_photo, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)
        

    def patch(self, request, pk):
        data= request.data
        product_photo = get_object_or_404(Product_Photo, pk=pk)
        serializer = self.serializer_class(instance=product_photo, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


    def delete(self, request, pk):
        ph = get_object_or_404(Product_Photo, pk=pk)
        ph.delete()
        return Response(data={"deleted":"product"}, status=status.HTTP_204_NO_CONTENT)