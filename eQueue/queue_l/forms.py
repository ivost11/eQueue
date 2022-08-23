from django import forms
from .models import QueueL


class AddQueueForm(forms.ModelForm):
    class Meta:
        model = QueueL
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }


class DeleteQueueForm(forms.ModelForm):
    class Meta:
        model = QueueL
        fields = ['title', 'email', ]
