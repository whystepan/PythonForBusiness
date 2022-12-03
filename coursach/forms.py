from django.forms import *
from .models import *


class TourForm(ModelForm):
    class Meta:
        model = TourPetition
        fields = ['last_name', 'first_name', 'middle_name', 'phone', 'email', 'date', 'persons_count']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control', 'id': 'firstName', 'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control', 'id': 'lastName', 'placeholder': 'Фамилия'
            }),
            'middle_name': TextInput(attrs={
                'class': 'form-control', 'id': 'middleName', 'placeholder': 'Отчество'
            }),
            'phone': TextInput(attrs={
                'class': 'form-control', 'id': 'phone', 'placeholder': '+7 8005553535'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control', 'id': 'email', 'placeholder': 'mail@mail.ru'
            }),
            'date': DateInput(attrs={
                'class': 'form-control', 'id': 'date', 'type': 'date'
            }),
            'persons_count': NumberInput(attrs={
                'class': 'form-control', 'id': 'persons'
            })
        }
