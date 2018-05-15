# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required  # To enable automatic login required functionality this login
from django.contrib.auth.mixins import LoginRequiredMixin  # Mixin is the decorator
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):    # The home page will be list of all the posts and it is going to inherit from ListView
    model = Post       # Connecting this to post model

    def get_queryset(self):
        # To get the list of Post/blog
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')   # Post.grab all
        # objects of the post and filter it based on the conditions given in brackets. Conditions are grab the
        # published date __ is the field query and lte is less than (actual field condition). So complete condition is
        # grab the published date which is less than or equal to the current time. and order them by published them by
        # published date. The dash (-) helps to order them in descending way else the oldest post will come first.
        # Refer to field lookups in django documentation.


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    # LoginRequiredMixin is same as @Login Required. @ is used for functions not for class based views
    login_url = '/login/'     # This field will take to the login page.
    redirect_field_name = 'blog/post_detail.html'     # This field will redirect to detail view
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')  # We don't want success url to activate before or during deleting the post,
    #  else it will redirect to another page of the website


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by()  # If the draft has not any publication date.



