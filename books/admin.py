from django.contrib import admin
from django.db import models
from .models import Book, Publisher, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'available', 'publication_year', 'author', 'isbn_no', 'publisher')
    list_filter = ('available', 'author')
    search_field = ('title', 'description', 'author', 'publisher')
    prepulated_fields = {}


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_field = ('name', 'short_name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_field = ('first_name', 'last_name')
