from django.db import models

from shop.models import Course
from user.models import User


class Purchase(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Course')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Buyer")
    total_price = models.FloatField(default=0.0, verbose_name="Total price")
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name="Purchase Date")
    courses_qty = models.PositiveIntegerField(default=0)




