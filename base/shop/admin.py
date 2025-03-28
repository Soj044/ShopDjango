from django.contrib import admin

from .models import Course, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category', 'created_at')


class CourseInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [CourseInline]
    fieldsets = [
        (None, {'fields': ['title']}),
        ('courses', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
