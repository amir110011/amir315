from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from blog.models import Post
from .mixins import *
# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all().order_by('-publish')
        else:
            return Post.objects.filter(author=self.request.user).order_by('-publish')


class PostCreate(LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
	model = Post
	template_name = "registration/post_create_update.html"


class PostUpdate(AuthorAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
	model = Post
	template_name = "registration/post_create_update.html"


class PostDelete(SuperUserAccessMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = "registration/post_confirm_delete.html"
