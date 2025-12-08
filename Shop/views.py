from django.shortcuts import render, redirect,  get_list_or_404, get_object_or_404
from django.contrib import messages
from django.views import View

from .models import CategoryModel, ProductModel

from .forms import AddCategoryForm, AddProductForm, AddProductStockForm

from django.http import HttpResponse
from django.utils.decorators import method_decorator

#admin required decorator
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Not allowed")

        if not request.user.is_superuser:
            return HttpResponse("Not allowed")

        return view_func(request, *args, **kwargs)

    return wrapper

# Create your views here.
class CategoryView(View):
    template_name = 'shop/category.html'
    def get(self, request):
        categories = CategoryModel.objects.all()
        return render(request, self.template_name, {'categories' : categories})

class ProductView(View):
    template_name = 'shop/products.html'
    
    def get(self, request, cat_id):
        cur_category = get_object_or_404(CategoryModel, pk = cat_id)
        return render(request, self.template_name, {'cur_category' : cur_category})

class ProductDetailsView(View):
    template_name = 'shop/product-details.html'
    
    def get(self, request, pro_id):
        cur_product = get_object_or_404(ProductModel, pk = pro_id)
        return render(request, self.template_name, {'cur_product' : cur_product})


@method_decorator(admin_required, name='dispatch')
class AddCategoryView(View):
    template_name = 'shop/admin/add-category.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form' : AddCategoryForm()})
    
    def post(self, request):
        form = AddCategoryForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'product added successfully')
            return redirect('shop:add-category')
        
        return render(request, self.template_name, {'form' : form})

@method_decorator(admin_required, name='dispatch')
class AddProductView(View):
    template_name = 'shop/admin/add-product.html'
    
    def get(self, request):
        return render(request, self.template_name, {'form' : AddProductForm})
    
    def post(self, request):
        form = AddProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('shop:add-product')
        
        return render(request, self.template_name, {'form' : form})

@method_decorator(admin_required, name='dispatch')
class AddProductStockView(View):
    template_name = 'shop/admin/add-stock.html'
    
    def get(self, request, pro_id):
        pro_stock = get_object_or_404(ProductModel, id = pro_id)
        form = AddProductStockForm(instance=pro_stock)
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request, pro_id):
        pro_stock = get_object_or_404(ProductModel, id=pro_id)
        form = AddProductStockForm(request.POST, instance=pro_stock)
        
        if form.is_valid():
            form.save()
            return redirect('shop:product-details', pro_id = pro_id)
        
        return render(request, self.template_name, {'form' : form})