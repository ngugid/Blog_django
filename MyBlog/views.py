from django.shortcuts import render
from .models import Blog1

# Create your views here.
def home(request):
    blogs = Blog1.objects.all()
    context = {
        'blogs' : blogs
    }
    return render(request, 'index.html', context)
