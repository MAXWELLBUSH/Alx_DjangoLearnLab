# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.query_samples import *
books_by_author("J.K. Rowling")

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(f"Book: {book.title} by {author.name}")

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(f"Book in {library.name}: {book.title} by {book.author.name}")

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")

# Example usage (uncomment to test)
# books_by_author("J.K. Rowling")
# books_in_library("City Library")
# librarian_for_library("City Library")