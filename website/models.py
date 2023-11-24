from django.db import models


class ProductCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Product Category'

    def __str__(self) -> str:
        return self.name
        #return f"{self.name}: {self.description}"

class Product(models.Model):
    category = models.ForeignKey("ProductCategory", models.CASCADE)
    #category = models.CharField("Product Category", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to= "products")
    #image_1 = models.ImageField(upload_to= "uploads/% Y/% m/% d/")
    image_1 = models.ImageField(upload_to= "uploads/images")
    image_2 = models.ImageField(upload_to= "uploads/images")
    image_3 = models.ImageField(upload_to= "uploads/images", null = True, blank = True)
    price = models.DecimalField(decimal_places= 2, max_digits= 8)
    top_selling = models.BooleanField(default=False)
    discount = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

