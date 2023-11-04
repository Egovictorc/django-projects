from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product-categories")
    # image = models.ImageField(upload_to= "products")
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Product(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to= "products")
    # image = models.FileField(upload_to= "products")
    price = models.DecimalField(decimal_places= 2, max_digits= 8)
    top_selling = models.BooleanField()
    discount = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"