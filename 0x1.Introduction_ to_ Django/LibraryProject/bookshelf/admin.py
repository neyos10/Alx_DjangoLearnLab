from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to search by in the admin interface
    search_fields = ('title', 'author')
    
    # Filters to enable on the right side of the admin interface
    list_filter = ('publication_year', 'author')

# Register the Book model with the custom admin configurations
admin.site.register(Book, BookAdmin)
