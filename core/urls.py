
from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('create/', views.create_item, name='create'),
 path('update/<int:pk>/', views.update_item, name='update'),
 path('delete/<int:pk>/', views.delete_item, name='delete'),
]
