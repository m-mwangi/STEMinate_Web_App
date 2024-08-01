# resources/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('<int:pk>/', views.resource_detail, name='resource_detail'),
    path('new/', views.resource_create, name='resource_create'),
    path('<int:pk>/edit/', views.resource_update, name='resource_update'),
    path('<int:pk>/delete/', views.resource_delete, name='resource_delete'),
]
