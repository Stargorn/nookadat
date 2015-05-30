from django.views import generic

from . import models


class BlogIndex(generic.ListView):
    queryset = models.Post.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = "post.html"

class TagIndex(generic.ListView):
    template_name = 'home.html'
    paginate_by = 2

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = models.Tag.objects.get(slug=slug)
        results = models.Post.objects.filter(tags=tag)
        return results
