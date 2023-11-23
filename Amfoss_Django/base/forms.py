from django import forms
from .models import Task

class TaskCompleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['complete']
        widgets = {'complete': forms.HiddenInput()}