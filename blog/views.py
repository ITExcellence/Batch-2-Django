from django.shortcuts import render

def home(request):
    posts = [
        {
        "title": "My First Post",
        "author": "Alice",
        },
        {
        "title": "Learning Django",
        "author": "Bob",
        },
        {
        "title": "Why Python Is Fun",
        "author": "Charlie",
        },
    ]
    
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

