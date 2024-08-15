```python

from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Confirm creation
print(book)

# Expected Output
<Book: 1984>