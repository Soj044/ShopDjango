from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('shop/<int:category_id>', views.single_category, name='cat_courses'),
    path('shop/', views.cat_index, name='cat_index'),
    path('<int:course_id>', views.single_course, name='single_course')
]