from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Weblog_setting, Slider
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request, page=1):
    post_list = Post.objects.filter(status="p").order_by("-publish")
    paginator = Paginator(post_list, 4)
    posts = paginator.page(page)
    context = {
        "post": posts,
        "about": Weblog_setting.objects.all(),
        "slid": Slider.objects.filter(status="p"), }
    return render(request, "blog/home.html", context)


def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    post_list = category.postcat.published()
    paginator = Paginator(post_list, 4)
    posts = paginator.get_page(page)
    context = {
        "categorys": category,
        "post": posts,
    }
    return render(request, "blog/category_list.html", context)


def author(request, username, page=1):
    author = get_object_or_404(User, username=username)
    post_list = author.post.published()
    paginator = Paginator(post_list, 4)
    posts = paginator.get_page(page)
    context = {
        "author": author,
        "post": posts,
    }
    return render(request, "blog/author_list.html", context)


def detail(request, slug ):
    context = {
        "post": get_object_or_404(Post.objects.published(), slug=slug),
        "about": Weblog_setting.objects.all(),
    }
    return render(request, "blog/detail.html", context)
