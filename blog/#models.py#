from django.db import models
from django_markdown.models import MarkdownField
import markdown2


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

    
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("tag_index", kwargs={"slug": self.slug})
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)    
    objects = PostQuerySet.as_manager()
    tags = models.ManyToManyField(Tag)

    def save(self):
        self.body_html = markdown2.markdown(self.body, extras=['fenced-code-blocks'])
        super(Post, self).save()
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ["-created"]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})


