from django.shortcuts import render
from django.views import View
from .models import Book


class MainPage(View):
    def get(self, request):
        top_sellers = Book.objects.all().order_by('-sell_count')[:3]
        print(top_sellers)
        context = {'top_sell': top_sellers}
        return render(request, "core/main_page.html", context)
