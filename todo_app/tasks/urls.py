from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todo-home'),
    path('about/', views.about, name='todo-about'),
    path('add_item/', views.add_item, name='add-todo'),
    path('update/<int:pk>/', views.update, name='todo-update'),
    path('delete/<int:pk>/', views.delete, name='todo-delete'),
]
