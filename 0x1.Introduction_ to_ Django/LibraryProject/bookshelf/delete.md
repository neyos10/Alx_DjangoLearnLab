
# Delete a Book Entry

## Django Shell

```python
# Import the Book model from bookshelf.models
from bookshelf.models import Book

# Delete the book entry
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected output:
# (1, {'bookshelf.Book': 1})

# Retrieve all books from the database
all_books = Book.objects.all()

# Print the list of all books
print(list(all_books))

# The output should be an empty list ([]), indicating that no books are present in the database.
