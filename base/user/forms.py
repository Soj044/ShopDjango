from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.utils import timezone

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

class UserProfileForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label="E-mail",
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    avatar = forms.ImageField(label='Avatar')
    # date_joined = forms.DateTimeField(label='Date joined', )

    class Meta:
        model = get_user_model()
        fields = ['avatar', 'username', 'email',]
        labels = {
            'username': 'name',
            'email': 'e-mail',
        }

class UserPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )
    new_password2 = forms.CharField(
        label='Повторите новый пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"})
    )
    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            "autofocus": True
        })
    )

    class Meta:
        labels = {
            'new_password1': 'Новый пароль',
            'new_password2': 'Повторите новый пароль',
            'old_password': 'Старый пароль',
        }


