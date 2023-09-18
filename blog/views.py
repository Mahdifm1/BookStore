from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog, Category, Tag


class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 5

    # context
    posts = Blog.objects.all().order_by('added_date')
    recent_posts = posts[:3]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    extra_context = {
        'posts': posts,
        'recent_posts': recent_posts,
        'categories': categories,
        'tags': tags
    }
