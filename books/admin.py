from django.contrib import admin

from .models import Book

# to show custom attributes we use modelAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")

admin.site.register(Book, BookAdmin)