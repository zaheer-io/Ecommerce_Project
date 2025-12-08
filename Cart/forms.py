from django import forms
from .models import OrderModel, OrderItemsModel

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ('address', 'phone', 'payment_method')