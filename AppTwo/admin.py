from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')  
    search_fields = ('name',)  
    list_filter = ('date_of_birth',) 
