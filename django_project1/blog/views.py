from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # HttpResponse is just a way to pass html code other than using templates
    # return HttpResponse('<h1>Blog Home</h1>')

    return render(request, 'blog/home.html')

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')

    return render(request, 'blog/about.html')


# the templates are structured as follows blog -> templates -> blog -> html page