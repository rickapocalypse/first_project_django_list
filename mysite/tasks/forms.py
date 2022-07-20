from django import forms
from .models import Task
from django.forms import TextInput, Textarea

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'class':'form-control'}),
        }
