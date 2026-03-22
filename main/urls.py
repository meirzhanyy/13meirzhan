from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('projects/<int:project_id>/', views.project_detail),
    path('info/', views.info),
]