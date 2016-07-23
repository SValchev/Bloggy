from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView

from .models import Post
from .forms import PostForm


class CustomListView(ListView):
    template_name = 'post/index.html'
    model = Post
    ordering = '-created'

    def get_context_data(self, **kwargs):
        context = super(CustomListView, self).get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context

# def list_posts(request):
#     all_posts = Post.objects.all().order_by('-created')
#     paginator = Paginator(all_posts, 3)
#     page = request.GET.get('page')
#
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         posts = paginator.page(paginator.num_pages)
#
#     context = {'posts':posts}
#
#     return render(request, 'post/index.html', context)

def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})

def edit_post(request, id=None):
    current_post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=current_post)
    if request.method == 'POST':
        if form.is_valid():
            with transaction.atomic():
                post = form.save(commit=False)
                post.save()
                messages.success(request, "Post has been updated successfuly!")
                return redirect(post)
            return HttpResponse("Something went wrong", status_code=400)
    context = {'form':form}
    return render(request, 'post/add.html', context)


def info_post(request, id=None):
    current_post = get_object_or_404(Post, id=id)
    context = {'post':current_post}

    return render(request, 'post/info.html', context)

def delete_post(request, id=None):
    current_post = None
    try:
        current_post = Post.objects.get(id=id)
        with transaction.atomic():
            current_post.delete()
            messages.success(request, "You have deleted the post successfuly")
            return redirect(reverse("post:index"))
        return HttpResponse("Could not delete the post!", status_code=400)
    except Post.DoesNotExist:
        messages.warning(request, "Post does not exists!")
        return redirect(reverse("post:index"))

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
