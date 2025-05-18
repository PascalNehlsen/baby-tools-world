from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=200, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name