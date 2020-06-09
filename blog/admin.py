from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "slug")
    list_filter = ("created_on",)
    data_hierarchy = "created_on"
    ordering = ("created_on",)
