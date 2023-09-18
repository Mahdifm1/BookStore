from django.shortcuts import render
from django.views import View, generic
from .models import Book, Category, Author


# get category item for given queryset
def get_categories_list(categories):
    context = []
    for category in categories:
        context.append({
            'name': category.name,
            'url': category.slug
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


def header_component(request):
    context = {'top_categories': get_categories()}
    return render(request, 'core/header.html', context)


def footer_component(request):
    return render(request, 'core/footer.html', {})


class MainPage(View):
    def get(self, request):
        books = Book.objects.all()
        top_sellers = books.order_by('-sell_count')[:4]
        latest_products = list(books.order_by('-added_date'))[:4]

        context = {'top_sell': top_sellers,
                   'top_featured': top_sellers,
                   'latest_products': latest_products}
        return render(request, "core/main_page.html", context)


class BookDetail(generic.DetailView):
    model = Book
    template_name = 'core/product_detail.html'


class ListCategories(generic.ListView):
    model = Book
    template_name = 'core/product_list.html'
    paginate_by = 15

    def get_queryset(self):
        if self.kwargs.get('sub_category'):
            return Book.objects.filter(category__slug__exact=self.kwargs.get('sub_category'),
                                       category__top_category__exact=self.kwargs.get('category'))
        else:
            return Book.objects.filter(category__top_category__exact=self.kwargs.get('category'))


class AuthorsListView(generic.ListView):
    model = Author
    template_name = 'core/author_list.html'
    paginate_by = 15
    authors = Author.objects.all()
    extra_context = {'authors': authors}


class About(View):
    def get(self, request):
        return render(request, 'core/about.html')


class ContactUs(View):
    def get(self, request):
        return render(request, 'core/contact_us.html')
