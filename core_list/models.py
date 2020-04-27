from django.db import models
from Authors_list.models import Authors


class Product(models.Model):
    name = models.CharField(max_length=100, null=True) 
    edition = models.PositiveIntegerField(null=True) 
    publication_year = models.IntegerField(null=True)   
    Authors = models.ManyToManyField(to=Authors)
    
def __str__(self):
    return self.name
