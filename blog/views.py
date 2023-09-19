from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog, Category, Tag


def sidebar(request):
    categories = Category.objects.all()
    context = {
        "recent_posts": Blog.objects.all().order_by('added_date')[:3],
        "left_categories": categories[:int(len(categories) / 2)],
        "right_categories": categories[int(len(categories) / 2):]
    }

    return render(request, 'blog/sidebar.html', context)


class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 5

    # context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Blog.objects.all().order_by('added_date')
        context["posts"] = posts
        return context


class Post(DetailView):
    model = Blog
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_comments"] = 3  # todo not complete
        return context
