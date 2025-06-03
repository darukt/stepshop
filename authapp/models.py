from django.contrib.auth.models import AbstractUser
from django.db import models

class ShopUser(AbstractUser):
    avatar = models.ImageField(
        verbose_name="Аватар",
        upload_to='avatars',
        blank=True
    )

    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        default=0,
    )