from django.contrib import admin
from .models import Category, Product, Inventory, Customer, Order, Product_Photo

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "desc")
    fields = [field.name for field in Category._meta.fields]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "desc", "price")
    fields = [field.name for field in Product._meta.fields]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("stock_status", "quantity", "product")
    fields = [field.name for field in Inventory._meta.fields]

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "addres", "email")
    fields = [field.name for field in Customer._meta.fields]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("total_price", )
    fields = [field.name for field in Order._meta.fields]

@admin.register(Product_Photo)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ("product", )
    fields = [field.name for field in Product_Photo._meta.fields]