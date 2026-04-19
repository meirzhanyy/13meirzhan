from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
    # №12 зертханалық жұмыс үшін жаңа жолдар:
    path('add-category/', views.add_category, name='add_category'), # Санат қосу [cite: 42]
    path('add-product/', views.add_product, name='add_product'), # Өнім қосу [cite: 43]
    path('product/<int:product_id>/add-review/', views.add_review, name='add_review'), # Пікір қалдыру [cite: 44]
]