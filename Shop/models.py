from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(_("Category Name"), max_length=50)
    category_image = models.ImageField(_("Category Image"), upload_to='category/images')
    category_description  = models.TextField(_("Category Description"))
    
    def __str__(self):
        return self.category_name

class ProductModel(models.Model):
    product_name = models.CharField(_("Product Name"), max_length=50)
    product_description = models.TextField(_("Product Description"))
    product_image = models.ImageField(_("Product Image"), upload_to='products/image')
    product_price = models.PositiveIntegerField(_("Product Price"))
    stock = models.PositiveIntegerField(_("Product Stock"))
    available = models.BooleanField(_("Product Availability"), default = True)
    created = models.DateTimeField(_("Created Time"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated Time"), auto_now=True)
    category = models.ForeignKey(CategoryModel, verbose_name=_("Category"), on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return f'{self.product_name} ({self.category.category_name})'