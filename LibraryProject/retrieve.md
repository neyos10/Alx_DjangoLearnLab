
# Retrieve a Book Entry

## Django Shell

```python
# Retrieve the book entry
book = Book.objects.get(title='1984')

# Print the details of the book
print(book.title, book.author, book.publication_year)

# Expected output:
1984 George Orwell 1949

# This output confirms that the book entry was successfully retrieved from the database