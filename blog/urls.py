from django.conf.urls import include, url

from . import views, feed


urlpatterns = [
    url(r'^tag/(?P<slug>\S+)$', views.TagIndex.as_view(), name="tag_index"),
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(),
        name="post_detail"),
    
]
