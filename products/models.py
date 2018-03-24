from django.db import models
import random
import os

# Create your models here

# PRE: filepath
# POST: return a parsed version of the filepath
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1, 1341231)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename = new_filename, ext = ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename = new_filename,
            final_filename = final_filename)

class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField()
    price       = models.DecimalField(default = 0.00, max_digits =7, decimal_places=2)
    picture     = models.ImageField(upload_to = upload_image_path, null=True, blank=True )

    def __str__(self):
        return self.title
