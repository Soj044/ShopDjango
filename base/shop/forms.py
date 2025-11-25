from django import forms
from .models import Course, Category


class CreateCourseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="не выбрана", label="Категория")

    class Meta:
        model = Course
        fields = ['title', 'course_slug', 'price', 'created_at', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input'}),
            'course_slug': forms.HiddenInput()
        }
        labels = {
            'title': 'Название курса',
            'course_slug': 'Slug',
            'price': 'Цена',
            'created_at': 'Дата создания',
            'category': 'Категория'
        }