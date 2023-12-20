import uuid
from django.db import models
from django.urls import reverse

class Book(models.Model):
    # for safer url routing like slug
    id = models.UUIDField(
        primary_key=True, 
        default = uuid.uuid4,
        editable = False
    )
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title
    
    # afno url afai return garne function 
    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])