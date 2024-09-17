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

#practiced in runserver shell
#     >>> from django.contrib.auth.models import User
#     >>> from blog.model import Post
#     Traceback (most recent call last):
#     File "<console>", line 1, in <module>
#     ModuleNotFoundError: No module named 'blog.model'
#     >>> from blog.models import Post 
#     >>> user = User.objects.get(username = 'admin')
#     >>> post = Post(title = 'Post 2 Title', slug = 'post-2-title', body = 'post 2 body', author = user)
#     >>> post.save()
#     >>> post.objects.create(title = 'Post 3 Title', slug = 'post-3-title', body = 'post 3 body', author = user)
#     Traceback (most recent call last):
#     File "<console>", line 1, in <module>
#     File "C:\Users\Darshan\Documents\Python\Blog Application Project\my_env\Lib\site-packages\django\db\models\manager.py", line 186, in __get__
#         raise AttributeError(
#     AttributeError: Manager isn't accessible via Post instances
#     >>> Post.objects.create(title = 'Post 3 Title', slug = 'post-3-title', body = 'post 3 body', author = user) 
#     <Post: Post 3 Title>
#     >>> Post.objects.all()
#     <QuerySet [<Post: Post 3 Title>, <Post: Post 2 Title>, <Post: Post 1 Title>]>
#     >>> Post.objects.filter(publish__year=2024)
#     <QuerySet [<Post: Post 3 Title>, <Post: Post 2 Title>, <Post: Post 1 Title>]>
#     >>> Post.objects.filter(publish__year=2024)\        
#     ... exclude(title__startswith="Post 2")
#     File "<console>", line 2
#         Post.objects.filter(publish__year=2024)\
#     exclude(title__startswith="Post 2")
#         ^^^^^^^
#     SyntaxError: invalid syntax
#     >>> Post.objects.filter(publish__year=2024)\
#     ... .exclude(title__startswith="Post 2")     
#     <QuerySet [<Post: Post 3 Title>, <Post: Post 1 Title>]>
#     >>> Post.object.order_by('title')
#     Traceback (most recent call last):
#     File "<console>", line 1, in <module>
#     AttributeError: type object 'Post' has no attribute 'object'
#     >>> Post.objects.order_by('title') 
#     <QuerySet [<Post: Post 1 Title>, <Post: Post 2 Title>, <Post: Post 3 Title>]>
#     >>> Post.objects.order_by('-title') 
#     <QuerySet [<Post: Post 3 Title>, <Post: Post 2 Title>, <Post: Post 1 Title>]>
#     >>> Post.object.get(id=1)
#     Traceback (most recent call last):
#     File "<console>", line 1, in <module>
#     AttributeError: type object 'Post' has no attribute 'object'
#     >>> Post.objects.get(id=1) 
#     <Post: Post 1 Title>
#     >>> delete Post.objects.get(id=1)  
#     File "<console>", line 1
#         delete Post.objects.get(id=1)
#             ^^^^
#     SyntaxError: invalid syntax
#     >>> delete_post = Post.objects.get(id=1)  
#     >>> delete_post.delete()
#     (1, {'blog.Post': 1})
#     >>> Post.objects.all                     
#     <bound method BaseManager.all of <django.db.models.manager.Manager object at 0x000001BCD0C76150>>
#     >>> Post.objects.all()
#     <QuerySet [<Post: Post 3 Title>, <Post: Post 2 Title>]>
#     >>> 
