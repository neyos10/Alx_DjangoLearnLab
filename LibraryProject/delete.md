
# Delete a Book Entry

## Django Shell

```python
# Delete the book entry
book.delete()

# expected output:
(1, {'bookshelf.Book': 1})

# Retrieve all books from the database
all_books = Book.objects.all()

# Print the list of all books
print(list(all_books))

# The output should be an empty list ([]), indicating that no books are present in the database