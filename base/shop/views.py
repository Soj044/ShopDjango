from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/index.html', {'courses': courses})
