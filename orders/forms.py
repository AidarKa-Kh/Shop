from django import forms
from .models import Order
INPUT_CLASSES = 'form-control'


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'contact', 'email', 'address', 'postal_code', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Фамилия'
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Телефон'
            }),
            'contact': forms.Select(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Мессенджер'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Почта'
            }),
            'address': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Адрес'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Индекс'
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Город'
            }),
        }
