from django.db import models
from products.models import Product
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    # A user can be associated with many carts.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # A product can be associated with many carts.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    total_price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
