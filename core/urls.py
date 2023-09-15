from django.urls import path
from core.views import MainPage, BookDetail, ListCategories, AuthorsListView, About, ContactUs

urlpatterns = [
    path('', MainPage.as_view(), name="main_page"),
    path('books/<int:pk>', BookDetail.as_view(), name="book_detail"),
    path('category/<str:category>', ListCategories.as_view(), name="list_categories"),
    path('authors/', AuthorsListView.as_view(), name="list_authors"),
    path('about/', About.as_view(), name='about'),
    path('contact-us/', ContactUs.as_view(), name='contact_us'),
]
