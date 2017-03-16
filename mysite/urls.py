"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
# from mysite.blog import views as blog_views

sitemaps = {
    'posts':PostSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 告诉Django在blog/路径下包含了blog应用中的urls.py定义的URL模式
    url(r'blog/',include('blog.urls',
                         namespace='blog',
                         app_name='blog')),
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

# url += [
#     url(r'^$',blog_views.post_list,name='post_list'),
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
#         blog_views.post_detail,
#         name='post_detail'),
# ]
