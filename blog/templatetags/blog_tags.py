from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

from ..models import Post

# @register.simple_tag(name='自定义标签名字')
# 返回字符串
@register.simple_tag
def total_post():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

# 将过滤器的名称改为markdown,函数名称改为markdown_format
# 使用{{ variable|markdown }}
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
