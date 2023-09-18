from django.db import models
from core.models import Category
from account.models import Profile


class Tag(models.Model):
    title = models.CharField(max_length=30)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='images/Blog/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    added_date = models.DateField(auto_now_add=True)


class Comment(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=150)
