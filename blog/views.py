from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all().order_by("-created_at")
    
    context = {
        "posts": posts,
    }

    return render(request, "blog/home.html", context)

# contact
def contact(request):
    return render(request, "blog/contact.html")

# about-us
def about(request):
    return render(request, "blog/about.html")

