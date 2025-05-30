from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    cat_slug = models.SlugField(max_length=255, unique=False, blank=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if not self.cat_slug:
            self.cat_slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    course_slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL")
    price = models.FloatField(default=0.0, blank=True)
    student_qty = models.PositiveIntegerField(default=0, blank=True)
    reviews_qty = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('shop:single_course', kwargs={'course_slug': self.course_slug})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.course_slug:
            self.course_slug = slugify(self.title)
        super().save(*args, **kwargs)
