from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from .models import Post


# class IndexView(generic.TemplateView):
#     template_name = "blog/post_list.html"


class PostListView(generic.ListView):
    context_object_name = "posts"
    template_name = "blog/post_list.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post


class AboutView(generic.TemplateView):
    template_name = "blog/about.html"
