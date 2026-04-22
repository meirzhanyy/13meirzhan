from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Category, Product


# ТІРКЕЛУ
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


# КІРУ
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Қате логин немесе пароль'})

    return render(request, 'login.html')


# ШЫҒУ
def logout_view(request):
    logout(request)
    return redirect('login')


# 🔐 БАСТЫ БЕТ (САНАТТАР)
@login_required
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


# 🔐 КАТАЛОГ (ӨНІМДЕР)
@login_required
def catalog(request, id):
    products = Product.objects.filter(category_id=id)
    return render(request, 'catalog.html', {'products': products})


# 🔐 САНАТ ҚОСУ
@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('home')
    
    return render(request, 'add_category.html')


# 🔐 ӨНІМ ҚОСУ
@login_required
def add_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category_id = request.POST.get('category')

        Product.objects.create(
            name=name,
            price=price,
            category_id=category_id
        )
        return redirect('home')

    return render(request, 'add_product.html', {'categories': categories})