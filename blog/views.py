from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Weblog_setting, Slider
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request, page=1):
    post_list = Post.objects.filter(status="p").order_by("-publish")
    paginator = Paginator(post_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    finally:
        context = {
            "post": posts,
            "about": Weblog_setting.objects.all(),
            "slid": Slider.objects.filter(status="p"), }
    return render(request, "blog/index.html", context)


def detail(request, slug):
    context = {
        "post": get_object_or_404(Post.objects.published(), slug=slug),
        "about": Weblog_setting.objects.all()

    }
    return render(request, "blog/detail.html", context)


def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    post_list = category.postcat.published()
    paginator = Paginator(post_list, 4)
    posts = paginator.get_page(page)

    context = {
        "categorys": category,
        "post": posts,
    }
    return render(request, "blog/category.html", context)
