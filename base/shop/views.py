from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import CreateCourseForm
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
class CreateCourse(PermissionRequiredMixin, CreateView):
    form_class = CreateCourseForm
    template_name = 'shop/create_course.html'
    permission_required = 'shop.add_course'

    def form_valid(self, form):
        course = form.save(commit=False)
        course.course_slug = slugify(course.title)
        course.save()
        return super().form_valid(form)


class CourseUpdateView(PermissionRequiredMixin, UpdateView):
    model = Course
    form_class = CreateCourseForm
    permission_required = 'shop.change_course'
    template_name = 'shop/edit_course.html'
    slug_url_kwarg = 'course_slug'
    success_url = reverse_lazy('shop:cat_index')

    def get_object(self, **kwargs):
        return get_object_or_404(Course, course_slug=self.kwargs[self.slug_url_kwarg])


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


class AllCoursesView(ListView):
    model = Course
    template_name = 'shop/all_courses.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all().order_by('id')
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)


class SearchCourse(ListView):
    template_name = 'shop/all_courses.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
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
