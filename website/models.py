from django.db import models


class ProductCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product-categories")
    # image = models.ImageField(upload_to= "products")
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to= "products")
    image_1 = models.FileField(upload_to= "products")
    image_2 = models.FileField(upload_to= "products")
    image_3 = models.FileField(upload_to= "products", null = True, blank = True)
    price = models.DecimalField(decimal_places= 2, max_digits= 8)
    top_selling = models.BooleanField(default=False)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"