

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(label = "Product Name", min_length=3)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Product Description", min_length=3)
    featured_image = forms.ImageField()
    image_1 = forms.ImageField()
    image_2 = forms.ImageField()
    image_3 = forms.ImageField()
    price = forms.DecimalField(decimal_places=2, max_digits=12)
    top_selling = forms.BooleanField()
    discount = forms.IntegerField()
    quantity = forms.IntegerField()
    class Meta:
        model = Product
        fields = ["name", "description", "featured_image", "price", "top_selling", "discount", "quantity", "image_1", "image_2", "image_3"]


