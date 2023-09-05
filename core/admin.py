from django.contrib import admin
from .models import Book, Author, Category


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'author', 'category', 'sell_count', 'added_date',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'number_of_books')

    def number_of_books(self, author):
        books = Book.objects.filter(author__exact=author)
        return len(books)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_books')

    def number_of_books(self, category):
        books = Book.objects.filter(category__exact=category)
        return len(books)
