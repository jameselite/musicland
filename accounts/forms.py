from .models import Customuser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = Customuser
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)