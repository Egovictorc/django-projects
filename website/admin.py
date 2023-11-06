# Register your models here.
from . import models
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name", "description", "price", "featured_image", "top_selling", "discount", "quantity")


admin.site.register(models.Product, ProductAdmin)