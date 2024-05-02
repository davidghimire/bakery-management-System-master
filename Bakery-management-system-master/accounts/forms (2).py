from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Home.models import Customer
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

