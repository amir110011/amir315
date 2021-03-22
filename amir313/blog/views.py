from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Weblog_setting
# Create your views here.


def home(request):
    context = {
        "post": Post.objects.filter(status="p").order_by("-publish")[:3],
        "about": Weblog_setting.objects.filter(status="1")
    }
    return render(request, "blog/index.html", context)


def detail(request, slug):
    context = {
        "post": get_object_or_404(Post, slug=slug, status="p")

    }
    return render(request, "blog/detail.html", context)


def category(request, slug):
    context = {
        "categorys": get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, "blog/category.html", context)
