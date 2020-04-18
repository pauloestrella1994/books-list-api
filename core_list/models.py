from django.db import models
from Authors_list.models import Authors


class Product(models.Model):
    name = models.CharField(max_length=100) 
    edition = models.PositiveIntegerField() 
    publication_year = models.DateField()    
    authors = models.ManyToManyField(Authors)
    
def __str__(self):
    return self.name
