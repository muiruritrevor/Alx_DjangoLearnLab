from relationship_app.models import Author, Book, Library,  Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    Author.objects.filter(author=author)
    books = Book.objects.filter(author_name=author_name)
    for book in books:
        print(f"Title: (book.title), Author: {book.author.name}")

def list_all_books(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        for book in books:
            print(f"Title: {book.title}, Author: {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

def retrieve_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")
        
