from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post) # if you want to just show post title
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish' , 'status'] # displays given attributes
    list_filter = ['status', 'created', 'publish', 'author'] # adds filter options for these attributes
    search_fields = ['title', 'body'] # adds search functionality for these attributes
    prepopulated_fields = {'slug': ('title',)} # automatically creates slug from title field
    raw_id_fields = ['author'] # allows to select objects from another model in the admin interface for related fields
    date_hierarchy = 'publish' # adds a date hierarchy filter for the publish field
    ordering = ['status', 'publish'] # changes the default ordering of the list view
    