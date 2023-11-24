from django.contrib.auth.models import User
from django import forms
from .models import Product, ProductCategory

class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(label = "Category Name", min_length=3)
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), label="Category Description", min_length=3)

    class Meta:
        model = ProductCategory
        fields = ["name", "description"]

class ProductForm(forms.ModelForm):
    #categories = [("Phones", "phones"),("Laptop", "laptop"),]
    categories = []
    try:
        #_categories = ProductCategory.objects.all().values()
        _categories = ProductCategory.objects.all()
        for _ in _categories:
            print(_)
            categories.append((_, _))
    except Exception as e:
        print(e)
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
    category = forms.ChoiceField(label="Product Category", choices=categories)
    class Meta:
        model = Product
        fields = ["name", "description", "featured_image", "price", "top_selling", "discount", "quantity", "image_1", "image_2", "image_3", "category"]


class UserForm(forms.ModelForm):
    user_categories = [("user", "User"), ("staff", "Staff")]
    first_name = forms.CharField(label = "First Name", min_length=3, widget = forms.TextInput(attrs={"placeholder": "eg: John"}))
    last_name = forms.CharField(label = "Last Name", min_length=3, widget = forms.TextInput(attrs={"placeholder": "eg: Doe"}))
    email = forms.EmailField(label = "Email Address", widget = forms.TextInput(attrs={"placeholder": "abc@gmail.com"}))
    #phone_number = forms.CharField(label = "Phone Number")
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)
    user_category = forms.ChoiceField(widget=forms.RadioSelect, choices=user_categories)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "user_category"]