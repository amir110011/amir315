from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Weblog_setting, Slider
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    post_list = Post.objects.filter(status="p").order_by("-publish")
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list,1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    finally:
        context = {
            "post": posts,
            "about": Weblog_setting.objects.filter(status="1"),
            "slid": Slider.objects.filter(status="p"), }
    return render(request, "blog/index.html", context)


def detail(request, slug):
    context = {
        "post": get_object_or_404(Post.objects.published(), slug=slug),
        "about": Weblog_setting.objects.filter(status="1")

    }
    return render(request, "blog/detail.html", context)


def category(request, slug):
    context = {
        "categorys": get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, "blog/category.html", context)
