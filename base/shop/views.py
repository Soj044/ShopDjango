from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *



def cat_index(request):
    category = Category.objects.all().order_by('id')
    return render(request, 'shop/cat_index.html', {'category': category})

def single_category(request, category_id):
    category_name = Category.objects.get(pk=category_id).name
    courses_by_cat = Course.objects.filter(category_id=category_id)
    return render(request, 'shop/single_category.html', {'courses': courses_by_cat, 'cat_name': category_name})

# def index(request):
#     courses = Course.objects.all()
#     return render(request, 'shop/single_category.html', {'courses': courses})

def single_course(request, course_id):
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/single_course.html', {'course': course})
    # except Course.DoesNotExist:
    #     raise Http404()
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})