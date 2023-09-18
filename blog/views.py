from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog, Category, Tag


class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 5

    # context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Blog.objects.all().order_by('added_date')
        context["posts"] = posts
        context["recent_posts"] = posts[:3]
        categories = Category.objects.all()
        context["left_categories"] = categories[:int(len(categories)/2)]
        context["right_categories"] = categories[int(len(categories)/2):]
        context["tags"] = Tag.objects.all()
        return context
