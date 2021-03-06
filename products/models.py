import os
import random
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from rshop.utils import unique_slug_generator
# Create your models here

# PRE: filepath
# POST: return a parsed version of the filepath
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# PRE: given a filepath
# POST: upload the image to the website from the filepath
def upload_image_path(instance, filename):
    new_filename = random.randint(1, 1341231)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename = new_filename,
            final_filename = final_filename
            )

# A custom queryset that manages every query to products database with different query operations
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)
    def active(self):
        return self.filter(active= True)

    def search(self,query):
        lookups = (Q(title__icontains = query) |
                   Q(description__icontains=query)|
                   Q(price__icontains = query)|
                   Q(producttag__title__icontains = query))

        return self.filter(lookups).distinct()

# Manages how every product is accessed from the database, works closely with above fun
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    def search(self,query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    title       = models.CharField(max_length = 120)
    timestamp   = models.DateTimeField(auto_now_add = True)
    slug        = models.SlugField(blank = True , unique = True) # makes the url more user friendly
    description = models.TextField()
    price       = models.DecimalField(default = 0.00, max_digits =7, decimal_places=2)
    picture     = models.ImageField(upload_to = upload_image_path, null=True, blank=True )
    featured    = models.BooleanField(default = False)
    active      = models.BooleanField(default = True)
    objects     = ProductManager()

    def __str__(self):
        return self.title + ": $" + str(self.price)

    def get_absolute_url(self):
        return reverse("products:detail", kwargs = {"slug": self.slug})

#Creates a unique slug for every product, even duplicated ones.
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
