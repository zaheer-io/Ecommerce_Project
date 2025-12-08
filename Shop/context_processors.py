from .models import CategoryModel

def links(request):
    categories = CategoryModel.objects.all()
    return {'links' : categories}