from django.conf.urls import url
from . import views as post_views

urlpatterns = [
    url(r'^$',post_views.post_list,name='post_list'),
    # url(r'^$',post_views.PostListView.as_view(),name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        post_views.post_detail,
        name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$',
        post_views.post_share,
        name='post_share'),
    url(r'^(?P<comment_id>\d+)/comment/$',post_views.comment_reply,name='comment_reply'),
    url(r'tag/(?P<tag_slug>[-\w]+)/$',post_views.post_list,name='post_list_by_tag'),
]