from django.urls import path, include
from . import views

urlpatterns = [
    # path("", views.IndexView.as_view(), name="home"),
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("tag/<slug:slug>/", views.TagListView.as_view(), name="tagged"),
    path("about", views.AboutView.as_view(), name="about"),
]
