from django.db import models

class GuestEmail(models.Model):
    email       = models.EmailField()
    timestamp   = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True, null=True, blank=True)
    active      = models.BooleanField(default = True)


    def __str__(self):
        return self.email
