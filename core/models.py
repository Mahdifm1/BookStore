from django.db import models


class Book(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    author = models.ForeignKey()
    category = models.ForeignKey()
    sell_count = models.IntegerField()
    img = models.ImageField()
    summary = models.TextField()


class Author(models.Model):
    name = models.CharField()
    age = models.IntegerField()
