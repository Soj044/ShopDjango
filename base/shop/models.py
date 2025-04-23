from django.utils import timezone

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    student_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title