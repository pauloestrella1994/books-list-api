from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100, null=True) 

def __str__(self):
    return self.name

    
    




