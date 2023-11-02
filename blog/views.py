from django.shortcuts import render, get_object_or_404
from .models import Category, Comment, Post, Tag


def home(request):
    obj_post = Post.objects.all()
    ctx = {
        'post': obj_post[:1],
    }
    return render(request, 'index.html', ctx)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def blog_grid(request):
    obj_post_list = Post.objects.all()
    ctx = {
        'list': obj_post_list,
    }
    return render(request, 'blog.html', ctx)


def blog_detail(request):
    obj_detail = Post.objects.all()
    ctx = {
        'detail': obj_detail,
    }
    return render(request, 'single.html', ctx)
