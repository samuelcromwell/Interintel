from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.sku}'
