from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]


class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]
