from django.contrib.auth.models import User
from django.db import models
from core.models import Book


class Cart(models.Model):
    books = models.ForeignKey(Book, models.CASCADE)


class profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    cart = models.ForeignKey(Cart, models.CASCADE)
    wallet = models.IntegerField(default=0, null=False)
