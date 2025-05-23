from django.contrib.auth.models import User
from django.db import models

def product_preview_dir_path(instance: "Product", filename: str) -> str:
    return f"products/product_{instance.pk}/preview/{filename}"

class Product(models.Model):
    class Meta:
        ordering = ['name', ]
    name = models.CharField(max_length=120, db_index=True)
    description = models.TextField(null=False, db_index=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    preview = models.ImageField(null=True, blank=True, upload_to=product_preview_dir_path)

    def __str__(self):
        return f'Product {self.name!r}'

def product_image_dir_path(instance: "ProductImage", filename: str) -> str:
    return f"products/product_{instance.product.pk}/images/{filename}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_dir_path)
    description = models.CharField(max_length=200, null=False, blank=True)


class Order(models.Model):
    delivery_address = models.TextField(null=False, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    receipt = models.FileField(null=True, upload_to='orders/receipts/')