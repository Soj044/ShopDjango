from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from base import settings
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPasswordChangeForm
from .models import *
from .services import PurchaseByUserService


class UserProfile(UpdateView, LoginRequiredMixin):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    extra_context = {'default_image': settings.DEFAULT_USER_IMAGE, }

    def get_success_url(self):
        return reverse('users:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Теперь подключаем покупки пользователя
        purchase_service = PurchaseByUserService()
        purchase = purchase_service.get_purchases(self.request.user.id)
        context['purchases'] = purchase  # Добавляем покупки в контекст
        return context

    def get_object(self, queryset=None):
        return self.request.user


# class RegisterUser(CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'user/register.html'
#     success_url = reverse_lazy('user:login')
#     extra_context = {
#         'title': "Registration"
#     }

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # ПОПРОБОВАТЬ УБРАТЬ ЭТО(ЧТО БУДЕТ???)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'user/register_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('shop:cat_index'))
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})

class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("user:change_pass_done")
    template_name = "user/password_change_form.html"

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))
