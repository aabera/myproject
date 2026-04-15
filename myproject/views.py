from django.shortcuts import render
from posts.models import Post

def homepage(request):
  
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')
