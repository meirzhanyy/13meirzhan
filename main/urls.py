from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/<int:id>/', views.catalog, name='catalog'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
]