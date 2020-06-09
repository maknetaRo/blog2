from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, default="", editable=False)
    text = models.TextField(max_length=70000)
    header_image = models.ImageField(upload_to="blog", blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    tags = TaggableManager()

    class Meta:
        ordering = ("-created_on",)

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        kwargs = {"slug": self.slug}
        return reverse("post_detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
