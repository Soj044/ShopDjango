from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from purchase.forms import PurchaseForm
from purchase.models import Purchase
from shop.models import Course


class CreatePurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    form_class = PurchaseForm
    template_name = 'purchase/purchase_form.html'
    success_url = reverse_lazy('shop:cat_index')  # или страница “успешной покупки”
    login_url = 'user:login'

    def dispatch(self, request, *args, **kwargs):
        self.course = get_object_or_404(Course, course_slug=self.kwargs['course_slug'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.buyer = self.request.user
        form.instance.course = self.course
        form.instance.total_price = self.course.price * form.instance.courses_qty
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = self.course
        return context
