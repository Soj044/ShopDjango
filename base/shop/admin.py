from django.contrib import admin

from purchase.models import Purchase
from .models import Course, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'price', 'category', 'created_at')


class CourseInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [CourseInline]
    fieldsets = [
        (None, {'fields': ['name']}),
        ('courses', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['buyer', 'course', 'total_price', 'purchase_date']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Purchase, PurchaseAdmin)
