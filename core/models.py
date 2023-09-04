from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    img = models.ImageField(upload_to="images/Authors/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

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

    def __str__(self):
        return f"{self.name}"
