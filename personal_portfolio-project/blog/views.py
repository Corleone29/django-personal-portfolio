from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # blogs = Blog.objects.all() # grabs objects from database
    # blogs = Blog.objects.order_by('-date')[:5]  # ordering objects by date, the latest one is first, also give only 5 last objects
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) 
    return render(request, 'blog/detail.html', {'blog': blog})