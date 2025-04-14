from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class business_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)  # Links to Django's User model
    business_name = models.CharField(max_length=255, blank=True, null=True)  # Business name, nullable
    business_email = models.EmailField(unique=True, blank=True, null=True, default='example@example.com')  # Email, nullable with default
    business_num = models.CharField(max_length=15, blank=True, null=True)  # Phone number, nullable
    business_location = models.TextField(blank=True, null=True)  # Address, nullable
    business_category = models.CharField(max_length=255, default='Unknown')  # Category, with default
    business_logo = models.ImageField(upload_to='business_logos/', blank=True, null=True)  # Optional logo
    opening_time = models.TimeField(blank=True, null=True)  # Nullable opening time
    closing_time = models.TimeField(blank=True, null=True)  # Nullable closing time
    def __str__(self):
        return self.business_name or "Unnamed Business"  # Avoid None if business_name is empty


class Product(models.Model):
    business = models.ForeignKey(business_profile, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=100)  # Product name, mandatory
    product_description = models.TextField()  # Product description, mandatory
    product_price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price, mandatory
    product_image = models.ImageField(upload_to='product_images/')  # Product image, mandatory
    is_available = models.BooleanField(default=True)  # Availability status
    added_on = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product is added

    def __str__(self):
        return f"{self.product_name} - {self.business.business_name}"
