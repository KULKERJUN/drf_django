from django.db import models

# Create your models here.

class ProductModel(models.Model):
    product_name = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    price = models.PositiveIntegerField(null=True)
    qty = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.product_name}'
