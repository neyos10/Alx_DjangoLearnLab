
# Update a Book Entry

## Django Shell

```python
# Update the book title
book.title = 'Nineteen Eighty-Four'
book.save()

# No output is expected after saving, but the book's title in the database is now updated to "Nineteen Eighty-Four"