from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Blog, Category, Comment
from .foms import CommentForm


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
        comments = Comment.objects.filter(blog__exact=self.object, is_accepted__exact=True).order_by('-added_date')
        context["count_comments"] = len(comments)
        context["comments"] = comments
        form = CommentForm(kwargs)
        context['form'] = form
        return context

    def post(self, *args, **kwargs):
        form = CommentForm(self.request.POST)
        if form.is_valid():
            blog = Blog.objects.get(slug__exact=kwargs.get('slug'))
            comment = Comment(name=form.cleaned_data.get('name'),
                              email=form.cleaned_data.get('email'),
                              description=form.cleaned_data.get('description'),
                              blog=blog)
            comment.save()

        return redirect(reverse("blog list") + self.kwargs.get('slug'))
