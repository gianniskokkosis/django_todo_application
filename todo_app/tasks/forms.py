from django import forms
from django.forms import ModelForm
from .models import TaskItem


class TaskItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size':'70', 'class':'mr-3 ml-3'}))
    status_completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'mr-3 ml-3'}))

    class Meta:
        model = TaskItem
        fields = '__all__'
