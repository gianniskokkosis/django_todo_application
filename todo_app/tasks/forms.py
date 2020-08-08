from django import forms
from django.forms import ModelForm
from .models import TaskItem


class TaskItemForm(models.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = TaskItem
        fields = '__all__'
