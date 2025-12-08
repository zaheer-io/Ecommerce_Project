from django import forms
from .models import CategoryModel, ProductModel

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class AddProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'

class AddProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['stock']
    
    