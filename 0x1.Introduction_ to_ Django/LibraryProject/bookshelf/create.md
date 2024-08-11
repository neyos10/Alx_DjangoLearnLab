
# Create a Bookshelf

## Django Shell

```python
from bookshelf.models import Book

# Create a new book entry
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)

# No output is expected after creating the entry, but the book is now stored in the database