from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product

class FeaturedProductListView(ListView):
    template_name = "products/featured/list.html"

    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.featured()

class FeaturedProductDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured/detail.html"


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    def get_queryset(self,*args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        obj = Product.objects.get_by_id(pk)
        # Similiar to what we do in product_detail_view
        if obj is None:
            raise Http404("The item you are searching for does not exist")
        return obj


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

def get_object(self, *args, **kwargs):
    request = self.request
    slug = self.kwargs.get('slug') # in url there is a slug as a keyword
    # Similiar to what we do in product_detail_view

    try:
        obj = Product.objects.get(slug= slug, active=True)
    except Product.DoesNotExist:
        raise Http404("Not Found")
    except Product.MultipleObjectsReturned:
        queryset = Product.objects.filter(slug=slug, active=True)
        obj = qs.first()
    except:
        raise Http404("Error ")
    return obj
