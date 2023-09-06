from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone

from core.models import Book


class Profile(AbstractUser):
    name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    wallet = models.IntegerField(default=0, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username


class Cart(models.Model):
    books = models.ForeignKey(Book, models.CASCADE)
    user = models.ForeignKey(Profile, models.CASCADE)
