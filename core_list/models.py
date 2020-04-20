from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100) 
    edition = models.PositiveIntegerField() 
    publication_year = models.DateField()    
    authors = models.CharField(max_length=100, null=True)
    
def __str__(self):
    return self.name
