from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import render , get_object_or_404,redirect

from django.contrib.auth import logout


def index(request):
    # Fetch all posts, ordered by ID in descending order
    posts = Blog.objects.order_by('-id')

    # Fetch the main post (the latest post where 'Main_post' is True)
    main_post = Blog.objects.filter(Main_post=True).order_by('-id')[:1]

    # Fetch recent posts, ordered by ID in descending order, limited to 5
    recent = Blog.objects.filter(section='Recent').order_by('-id')[:5]

    # Fetch popular posts
    popular = Blog.objects.filter(section='popular').order_by('-id')[0:5]
    
    # Fetch all categories
    category = Category.objects.all()

    # Create the context dictionary
    context = {
        'posts': posts,
        'main_post': main_post,
        'recent': recent,
        'category': category,
        'popular': popular,  # Include the popular posts in the context
        'carousel_posts': posts[:5]  # Limit the number of posts for the carousel (e.g., top 3 posts)
    }

    # Pass the context to the 'index.html' template
    return render(request, 'index.html', context)

def blog_detail(request,slug):
    # posts=Blog.objects.order_by('-id')
    category=Category.objects.all()
    post = get_object_or_404(Blog,blog_slug=slug)
    comments= Comment.objects.filter(blog_id=post.id).order_by('-date')
    context = {
        # 'posts': post,
        'category': category,  
        'post': post,
        'comments':comments
    }
    return render(request, 'blog_detail.html', context)
def category(request, slug):
    # Fetch all categories
    cat = Category.objects.all()

    # Fetch all blog posts for the active category using the slug
    blog_cat = category.objects.filter(slug=slug)

    # Create a context dictionary
    context = {
        'cat': cat,
        'active_category': slug,
        'blog_cat': blog_cat
    }

    # Render the template
    return render(request, 'category.html', context)

def about(request):
    return render(request, 'about.html')  # Render the about.html template
def contact(request):
    return render(request, 'contact.html')

def add_comment(request, slug):
    if request.method == 'POST':
        post = get_object_or_404(Blog, blog_slug=slug)

        # Retrieve data from the POST request
        comment_text = request.POST.get("InputComment")  # Input name for comment
        email = request.POST.get("InputEmail")           # Input name for email
        website = request.POST.get("InputWeb")           # Input name for website
        name = request.POST.get("InputName")             # Input name for name
        parent_id = request.POST.get('parent_id')

        parent_comment = None
        if parent_id:
            parent_comment = get_object_or_404(Comment, id=parent_id)

        # Create the comment using the correct field names
        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            website=website,
            comment=comment_text,  # Correct field name is 'comment'
            parent=parent_comment,
            date=timezone.now()  # Set the date explicitly
        )

        return redirect('blog_detail', slug=post.blog_slug)

    return redirect('blog_detail')


# def force_logout_and_login(request):
#     logout(request)
#     return redirect('admin:login')  # Redirect to the Django admin login


def force_logout_and_login(request):
    # Logs the user out
    logout(request)
    # Redirects to the admin login page with a 'next' parameter that redirects to the dashboard after login
    return redirect('/admin/login/?next=/dashboard/')