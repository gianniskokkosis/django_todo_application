from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TaskItem

def home(request):
    todos = TaskItem.objects.all().order_by('-date_added')
    context = {
        'todos': todos
    }
    return render(request, 'tasks/home.html', context)


def about(request):
    return render(request, 'tasks/about.html')


def add_item(request):
    new_item = request.POST['add_todo']
    TaskItem.objects.create(title=new_item)
    return HttpResponseRedirect('/')

def update(request):
    return HttpResponse('<h1>Update Item</h1>')


def delete(request):
    return  HttpResponse('<h1>Delete Item</h1>')
