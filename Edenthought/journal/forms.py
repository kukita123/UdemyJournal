from pyexpat import model
from tkinter import Widget

from django.forms import ModelForm

# - Registration (create user)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# - Login (authentication)
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Work with model Thought
from .models import Thought


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class ThoughtPostForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['title', 'content',]
        exclude = ['user']
