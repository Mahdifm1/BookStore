from django.urls import path
from .views import BlogList,Post

urlpatterns = [
    path('', BlogList.as_view(), name='blog list'),
    path('<slug:slug>', Post.as_view(), name='post'),
]
