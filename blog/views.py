from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    
    context = {
        "posts": posts,
    }

    return render(request, "blog/home.html", context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        "post": post,
    }

    return render(request, "blog/post_detail.html", context)
# contact
def contact(request):
    return render(request, "blog/contact.html")

# about-us
def about(request):
    return render(request, "blog/about.html")


