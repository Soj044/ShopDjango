from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.db import models

from shop.services import get_discounted_price


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
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00, blank=True)
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
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

    def get_discounted_price(self):
        return get_discounted_price(self)
