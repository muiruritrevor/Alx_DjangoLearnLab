from django.db import models

class Author(models.Model):
    # stores the name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    # stores the title of the book
    title = models.CharField(max_length=150)
    # stores the year of the book was published
    publication_year = models.IntegerField()
    # Links the book to an author, establishing a one-to-many relationship
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books")

    def __str__(self):
        return self.title
    