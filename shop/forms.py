from django import forms
from .models import Message

INPUT_CLASSES = 'form-control'


class UsersMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваш email'
            }),
            'message': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Ваше сообщение'
            })
        }
