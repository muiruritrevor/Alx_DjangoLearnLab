from django.db import models

class Boook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self): 
        return self.name
# Create your models here.
