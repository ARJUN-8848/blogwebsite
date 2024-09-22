from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    # Define status choices
    STATUS_CHOICES = (
        ('0', 'DRAFT'),
        ('1', 'PUBLISH'),
    )
    SECTION = (
        ('Recent', 'Recent'),
        ('popular', 'popular'),
        ('Trending', 'Trending')
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images', blank=True, null=True)  # Field for author image
    image = models.ImageField(upload_to='images')
    featured_image = models.ImageField(upload_to='featured_images', blank=True, null=True)  # Field for featured image
    featured_image1 = models.ImageField(upload_to='featured_images', blank=True, null=True)  # Field for featured image
    featured_image2 = models.ImageField(upload_to='featured_images', blank=True, null=True)  # Field for featured image


    introduction = models.TextField()  # Existing field for introduction
    heading1 = models.CharField(max_length=255, blank=True, null=True)  # New field for h3 heading
    heading2 = models.CharField(max_length=255, blank=True, null=True)  # New field for h3 heading
    authorname = models.CharField(max_length=255, blank=True, null=True)  # New field for h3 heading


    content1 = models.TextField(blank=True, null=True)  # New field for additional content
    content2 = models.TextField(blank=True, null=True)  # New field for additional content
    Conclusion= models.TextField(blank=True, null=True)  # New field for additional content


    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    blog_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    date = models.DateField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='0')
    section = models.CharField(choices=SECTION, max_length=100)
    Main_post = models.BooleanField(default=False)
    views = models.PositiveBigIntegerField(default=0)


    def __str__(self):
        return f"{self.title}({self.category})"



class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    
    # ForeignKey linking the comment to a specific blog post
    post = models.ForeignKey(
        'Blog', 
        related_name='comments', 
        on_delete=models.CASCADE
    )

    # Optional blog id, for extra identification
    blog_id = models.IntegerField(blank=True, null=True)
    
    # Name of the commenter
    name = models.CharField(max_length=100)

    # Email field for the commenter
    email = models.EmailField()

    # Optional website field for the commenter
    website = models.URLField(blank=True, null=True)

    # Comment content
    comment = models.TextField()

    # Date when the comment was made
    date = models.DateField(default=timezone.now)

    # Parent comment for threaded replies
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name='replies'
    )

    def save(self, *args, **kwargs):
        # Ensure the blog_id is set based on the post before saving
        if self.post:
            self.blog_id = self.post.id
        super().save(*args, **kwargs)

    def __str__(self):
        # String representation of the Comment object
        return self.name
  