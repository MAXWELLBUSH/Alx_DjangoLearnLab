# Create Book Instance

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>


Do the same for **retrieve.md, update.md, delete.md**.  
Then make a **CRUD_operations.md** that combines all four.

---

### ✅ Step 3: Admin Setup
In `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)
