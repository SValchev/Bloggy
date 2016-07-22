from django.shortcuts import render, get_object_or_404

from .models import Post

# Create your views here.

def list_posts(request):
    all_posts = Post.objects.all()
    context = {'posts':all_posts}
    return render(request, 'post/index.html', context)

def edit_post(request):
    pass

def info_post(request, id=None):
    current_post = get_object_or_404(Post, id=id)
    context = {'post':current_post}
    return render(request, 'post/info.html', context)

def delete_post(request):
    pass

def add_post(request):
    pass
