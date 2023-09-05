from django.shortcuts import render
from django.views import View
from .models import Book


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
                   'latest_products': latest_products}
        return render(request, "core/main_page.html", context)
