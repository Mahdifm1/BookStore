from django.shortcuts import render
from django.views import View, generic
from .models import Book, Category, Author


# get category item for given queryset
def get_categories_list(categories):
    context = []
    for category in categories:
        context.append({
            'name': category.name,
            'url': '_'.join(category.name.split())  # replace space with '_' in name
        })
    return context


# get categories names and titles from db
def get_categories():
    categories = Category.objects.all()
    top_categories = categories.values('top_category')
    top_categories = list(set([(list(key.values()))[0] for key in top_categories]))
    sorted(top_categories)

    context = []
    for top in top_categories:
        context.append({
            'top_category_name': top,
            'categories': get_categories_list(list(categories.filter(top_category__exact=top)))
        })

    context = sorted(context, key=lambda x: x['top_category_name'])
    return context


class MainPage(View):
    def get(self, request):
        books = Book.objects.all()
        top_sellers = books.order_by('-sell_count')[:4]
        latest_products = list(books.order_by('-added_date'))[:4]

        context = {'top_sell': top_sellers,
                   'top_featured': top_sellers,
                   'latest_products': latest_products,
                   'top_categories': get_categories()}
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


class ContactUs(View):
    def get(self, request):
        return render(request, 'core/contact_us.html')
