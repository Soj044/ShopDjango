from random import Random

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from . import views
from .views import UserPasswordChangeView

app_name = 'user'
urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password-change', UserPasswordChangeView.as_view(), name='change_pass'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"),
                                                                name='change_pass_done')
]