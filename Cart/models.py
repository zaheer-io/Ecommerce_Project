from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from Shop.models import ProductModel  

# Create your models here.
class CartModel(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User Details"), on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(ProductModel, verbose_name=_("Product Details"), on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_("Quantity"))
    date_added = models.DateTimeField(_("Date Added"), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f'{self.product.product_name} ({self.user.username})'
    
    def sub_total(self):
        return self.product.product_price * self.quantity

class OrderModel(models.Model):
    
    payment_choices = [
        ('Cash On Deliver', 'Cash on Deliver'),
        ('Pay Online', 'Pay Online'),
    ]
    
    order_id = models.CharField(_("Order id"), max_length=50, blank=True)
    user = models.ForeignKey(User, verbose_name=_("User Details"), on_delete=models.CASCADE, related_name='orders')
    amount = models.IntegerField(_("Order Amount"))
    address = models.TextField(_("Customer Address"))
    phone = models.IntegerField(_("Customer Phone Number"))
    payment_method = models.CharField(_("Payment Method"), max_length=50, choices=payment_choices)
    order_date = models.DateField(_("Ordering Date"), auto_now=False, auto_now_add=True)
    is_ordered = models.BooleanField(_("Is ordered"), default=False)
    delivery_status = models.CharField(_("Delivery Status"), default='pending', max_length=50)

    def __str__(self):
        return f'{self.user.username, self.amount}'

class OrderItemsModel(models.Model):
    order = models.ForeignKey(OrderModel, verbose_name=_("Order Details"), on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey("Shop.ProductModel", verbose_name=_("Product Details"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Order Quantity"))
    
    def __str__(self):
        return f'{self.product.product_name}, {self.order.user.username}'
    