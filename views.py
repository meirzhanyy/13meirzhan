from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Review

# Басты парақша (санаттар тізімі)
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

# Каталог (тауарлар тізімі)
def catalog(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'catalog.html', {'category': category, 'products': products})

# Тауардың толық сипаттамасы
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})