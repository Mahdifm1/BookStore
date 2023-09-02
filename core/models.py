from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    img = models.ImageField(upload_to="Authors/")


class Category(models.Model):
    name = models.CharField(max_length=30)


class Book(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    author = models.ForeignKey(Author, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    sell_count = models.IntegerField()
    img = models.ImageField(upload_to="Books/")
    summary = models.TextField()
