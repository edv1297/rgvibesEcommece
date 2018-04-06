from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

# Create your views here.

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self,*args,**kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        if context['query'] == None:
            context['query'] = ' '
        return context

    def get_queryset(self,*args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
         #icontains, field contains this (ignore case), iexact has to be an exact ma
