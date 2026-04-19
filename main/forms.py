from django import forms
from .models import Category, Product, Review

# 1. Санат қосу формасы
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': 'Санат атауы'}

# 2. Өнім қосу формасы
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'category']
        labels = {
            'name': 'Өнім атауы',
            'price': 'Бағасы (тг)',
            'quantity': 'Қоймадағы саны',
            'category': 'Санаты'
        }

# 3. Пікір қосу формасы
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {'text': 'Пікіріңіз'}
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Осында жазыңыз...'}),
        }