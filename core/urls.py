from django.urls import path
from core.views import MainPage, BookDetail, ListCategories

urlpatterns = [
    path('', MainPage.as_view(), name="main_page"),
    path('books/<int:pk>', BookDetail.as_view(), name="book_detail"),
]
