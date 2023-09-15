from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    img = models.ImageField(upload_to="images/Authors/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)
    top_category = models.CharField(max_length=30, null=False, default="category")
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(null=False)
    author = models.ForeignKey(Author, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    sell_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to="images/Books/", null=True)
    summary = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
