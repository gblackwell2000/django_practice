from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'GilbertB',
        'title' : 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'aunonymous',
        'title' : 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    # HttpResponse is just a way to pass html code other than using templates
    # return HttpResponse('<h1>Blog Home</h1>')

    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')

    return render(request, 'blog/about.html', {'title': 'About'})


# the templates are structured as follows blog -> templates -> blog -> html page