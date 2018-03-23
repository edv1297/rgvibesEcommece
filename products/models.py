from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField()
    price       = models.DecimalField(default = 0.00, max_digits =7, decimal_places=2)
    picture     = models.ImageField(upload_to = 'pic_folder',default = 'pic_folder/None/no-img.jpg' )

    def __str__(self):
        return self.title
