from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.objects.filter(status=1).count()


@register.inclusion_tag("blog/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.objects.filter(status=1).order_by("-created_on")[:count]
    return {"latest_posts": latest_posts}
