from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


class BlogList(ListView):
    model = Blog
