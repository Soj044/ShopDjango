from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.ShopHome.as_view(), name='cat_index'),
    path('category/<slug:cat_slug>/', views.SingleCategory.as_view(), name='cat_courses'),
    path('course/<slug:course_slug>/', views.SingleCourse.as_view(), name='single_course'),
    path('create-course/', views.CreateCourse.as_view(), name='create_course'),
    path('edit-course/<slug:course_slug>/', views.CourseUpdateView.as_view(), name='edit_course'),
    path('search/', views.SearchCourse.as_view(), name='search'),
    path('all-courses', views.AllCoursesView.as_view(), name='all_courses')
]