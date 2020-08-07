from django.shortcuts import render
from .models import TaskItem

def home(request):
    todos = TaskItem.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'tasks/home.html', context)

def about(request):
    return render(request, 'tasks/about.html')
