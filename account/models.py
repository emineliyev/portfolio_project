from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='user/%Y/%m/%d/', verbose_name='Şəkil', null=True, blank=True)

