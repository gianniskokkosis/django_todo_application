from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskItem

def home(request):
    todos = TaskItem.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'tasks/home.html', context)


def about(request):
    return render(request, 'tasks/about.html')


def add_item(request):
    return HttpResponse('<h1>Add Item</h1>')

def update(request):
    return HttpResponse('<h1>Update Item</h1>')


def delete(request):
    return  HttpResponse('<h1>Delete Item</h1>')
