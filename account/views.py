from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Post
# Create your views here.



class PostList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.Post.objects.all()
        else:
            return self.Post.objects.filter(author=self.request.user)


