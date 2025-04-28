from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('shop/', views.ShopHome.as_view(), name='cat_index'),
    path('shop/category/<slug:cat_slug>/', views.SingleCategory.as_view(), name='cat_courses'),
    path('shop/course/<slug:course_slug>/', views.SingleCourse.as_view(), name='single_course'),
]