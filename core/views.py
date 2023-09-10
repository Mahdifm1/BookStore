from django.shortcuts import render
from django.views import View, generic
from .models import Book, Category, Author


def get_categories():
    return Category.objects.all()


class MainPage(View):
    def get(self, request):
        books = Book.objects.all()
        top_sellers = books.order_by('-sell_count')[:3]
        latest_products_query = list(books.order_by('-added_date'))[:12]
        latest_products = []
        pr = []
        for i in range(len(latest_products_query)):
            pr.append(latest_products_query[i])
            if (i + 1) % 4 == 0:
                latest_products.append(pr)
                pr = []

        context = {'top_sell': top_sellers,
                   'latest_products': latest_products,
                   'categories': get_categories()}
        return render(request, "core/main_page.html", context)


class BookDetail(generic.DetailView):
    model = Book
    extra_context = {'categories': get_categories()}
    template_name = 'core/product_detail.html'


class ListCategories(generic.ListView):
    model = Book
    template_name = 'core/product_list.html'
    paginate_by = 15
    extra_context = {'categories': get_categories()}

    def get_queryset(self):
        return Book.objects.filter(category__name__exact=self.kwargs.get('name'))


class AuthorsListView(generic.ListView):
    model = Author
    template_name = 'core/author_list.html'
    paginate_by = 15
    authors = Author.objects.all()
    extra_context = {'categories': get_categories(),
                     'authors': authors}


class About(View):
    def get(self, request):
        return render(request, 'core/about.html')
