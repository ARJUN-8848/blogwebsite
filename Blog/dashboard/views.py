from django.shortcuts import render
from django.http import HttpResponse
from HOME.models import *
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/admin/login/') 
def dashboard(request):
    # Calculate total views across all blogs
    total_views = Blog.objects.aggregate(total_views=Sum('views'))["total_views"]

    # Count total number of comments
    total_comments = Comment.objects.count()

    # Count total number of blog posts
    total_posts = Blog.objects.count()

    # Get the latest blog posts, ordered by ID in descending order
    post = Blog.objects.order_by('-id')

    # Prepare context data for rendering
    context = {
        "total_views": total_views,
        "total_comments": total_comments,
        "total_posts": total_posts,
        "post": post,
    }

    # Render the dashboard template
    return render(request, "dashboard/dash.html", context)

@login_required

def blog(request):
    post=Blog.objects.order_by('-id')
    context={
        'post':post
    }
    return render (request,"dashboard/dash_blog.html",context)

@login_required

def comment(request):
    all_comments = Comment.objects.select_related('post').order_by('date')
    context = {
        'all_comments':all_comments
    }
    return render (request,"dashboard/commnets.html",context)


@login_required

def page(request):
    return render (request,"dashboard/pages.html")

