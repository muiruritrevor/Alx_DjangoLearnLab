# Python command to delete the book
 ```python

from bookshelf.model import Book

 # delete the book created
retrieved_book.delete()

#confirm deletion
books = Book.objects.all()
print(books)
 
#Expected Output