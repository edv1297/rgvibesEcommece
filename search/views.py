from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_queryset(self,*args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.filter(title__icontains = query)
        return Product.objects.featured()
         #icontains, field contains this (ignore case), iexact has to be an exact ma
