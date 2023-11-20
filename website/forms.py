
from django.contrib.auth.models import User
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


class UserForm(forms.ModelForm):

    user_categories = [("user", "User"), ("staff", "Staff")]
    first_name = forms.CharField(label = "First Name", min_length=3)
    last_name = forms.CharField(label = "Last Name", min_length=3)
    email = forms.EmailField(label = "Email Address")
    #phone_number = forms.CharField(label = "Phone Number")
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)
    user_category = forms.ChoiceField(widget=forms.RadioSelect, choices=user_categories)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "user_category"]


