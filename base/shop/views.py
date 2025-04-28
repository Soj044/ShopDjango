from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView

from .models import *


class ShopHome(ListView):
    template_name = 'shop/cat_index.html'
    title_page = 'CourseShop'
    context_object_name = 'category'

    def get_queryset(self):
        return Category.objects.all().order_by('id')

# def cat_index(request):
#     category = Category.objects.all().order_by('id')
#     return render(request, 'shop/cat_index.html', {'category': category})


class SingleCategory(ListView):
    model = Course
    template_name = 'shop/single_category.html'
    context_object_name = 'courses'
    slug_url_kwarg = 'cat_slug'

    def get_queryset(self):
        self.category = get_object_or_404(Category, cat_slug=self.kwargs[self.slug_url_kwarg])
        return Course.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_name'] = self.category.name  # передать имя категории
        return context

# def single_category(request, cat_slug):
#     category = get_object_or_404(Category, cat_slug=cat_slug)
#     courses_by_cat = Course.objects.filter(category=category)
#     return render(request, 'shop/single_category.html', {'courses': courses_by_cat, 'cat_name': category})

# def index(request):
#     courses = Course.objects.all()
#     return render(request, 'shop/single_category.html', {'courses': courses})

class SingleCourse(DetailView):
    template_name = 'shop/single_course.html'
    context_object_name = 'course'
    slug_url_kwarg = 'course_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Course, course_slug=self.kwargs[self.slug_url_kwarg])
