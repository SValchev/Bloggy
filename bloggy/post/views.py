from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    template_name = 'post/index.html'
    model = Post
    context_object_name = 'posts'
    ordering = '-created'
    paginate_by = 2


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post/add.html'
    form_class = PostForm
    model = Post
    pk_url_kwarg = 'id'


class PostDetailView(DetailView):
    template_name = 'post/info.html'
    model = Post
    queryset = None
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('post:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post/add.html'
    form_class = PostForm
