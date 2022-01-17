from django.contrib import admin

# Register your models here.
from .models import Book,Author
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display=('title','price','isAvailable','author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','date_of_birth','date_of_death')