from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    avatar = models.ImageField(upload_to="user_photos/%Y/%m/%d/",
                               verbose_name="Фото профиля", blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.username