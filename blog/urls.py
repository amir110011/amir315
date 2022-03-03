
from django.urls import path
from .views import home, detail, category, author

app_name = "blog"

urlpatterns = [
    path('', home, name="home"),
    path('page/<int:page>', home, name="home"),
    path('post/<slug:slug>', detail, name="detail"),
    path('category/<slug:slug>', category, name="category"),
    path('category/<slug:slug>/page/<int:page>', category, name="category"),
    path('author/<slug:username>', author, name="author"),
    path('author/<slug:username>/page/<int:page>', author, name="author"),
]
