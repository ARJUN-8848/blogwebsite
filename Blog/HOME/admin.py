from django.contrib import admin
from .models import Blog, Category,Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date')
    exclude = ('blog_slug', 'date')  # Exclude non-editable fields
    fields = ('title', 'author', 'author_image', 'image', 'featured_image', 'featured_image1', 'featured_image2', 'introduction', 'heading1','heading2', 'content1', 'content2', 'Conclusion', 'category', 'status', 'section', 'Main_post','authorname')
    search_fields = ('title', 'author')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)

