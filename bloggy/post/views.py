from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.db import transaction
from django.contrib import messages

from .models import Post
from .forms import PostForm


def list_posts(request):
    all_posts = Post.objects.all().order_by('-created')
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
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            with transaction.atomic():
                post = form.save(commit=False)
                post.save()
                messages.success(request, "Post has been added successfuly!")
                return redirect(post)
            return HttpResponse("Something went wrong", status_code=400)
    context = {'form':form}
    return render(request, 'post/add.html', context)
