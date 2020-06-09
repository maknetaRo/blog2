from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from taggit.models import Tag

from .models import Post


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class TagListView(TagMixin, generic.ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/post_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get("slug"))


class PostListView(TagMixin, generic.ListView):
    context_object_name = "posts"
    template_name = "blog/post_list.html"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 10


class PostDetailView(TagMixin, generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["similar_posts"] = self.object.tags.similar_objects()[:3]
        return context


class AboutView(TagMixin, generic.TemplateView):
    template_name = "blog/about.html"
