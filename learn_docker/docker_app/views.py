from django.shortcuts import render
from .models import Blog, Author

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'learn_docker/blog_list.html', {'blogs': blogs})
