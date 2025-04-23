from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {'email': 'E-mail'}

