from django.db import models
from core.models import Category


class Comment(models.Model):
    pass


class Tag(models.Model):
    pass


class Blog(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/Blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
