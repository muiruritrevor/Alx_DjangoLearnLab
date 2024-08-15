from django.db import models

# Creating a 'Book' model
class Book(models.Model):
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
