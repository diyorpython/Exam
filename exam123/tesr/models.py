from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ManyToManyField(to=Category)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    desc = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
class Inventory(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    stock_status = models.BooleanField(default=False)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.product
    
class Product_Photo(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    thumbnail_pc = models.ImageField(upload_to="media/thumblin/")
    large_pc = models.ImageField(upload_to="media/large/")

    def __str__(self) -> str:
        return self.product
    

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=55)
    addres = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.full_name
    
class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(to=Product)
    total_price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.customer