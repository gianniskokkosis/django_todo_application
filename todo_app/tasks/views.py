from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import TaskItem
from .forms import TaskItemForm

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

def update(request, pk):
    obj = TaskItem.objects.get(id=pk)
    form = TaskItemForm(instance=obj)

    if request.method == 'POST':
        form = TaskItemForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        'form': form,
        'obj': obj
    }
    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    deleted_obj = TaskItem.objects.get(id=pk)

    if request.method == 'POST':
        deleted_obj.delete()
        return HttpResponseRedirect('/')

    context = {
        'obj': deleted_obj
    }
    return  render(request, 'tasks/delete.html', context)
