from django.shortcuts import render,get_object_or_404
from .models import Post,Comment,Reply
from taggit.models import Tag
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm,ReplyForm
from django.core.mail import send_mail
from django.db.models import Count
from django.http import HttpResponsePermanentRedirect
# Create your views here.

# 基于ListView类的post_List视图
# 功能类似post_list视图
# 不是很懂

class PostListView(ListView):
    queryset = Post.published.all()         # 指定查询集合为全部Post对象
    context_object_name = 'posts'           # 环境变量posts赋给context_object_name,不指定变量则默认是object_List
    paginate_by = 2                         # 每页只显示3个对象
    template_name = 'blog/post/list.html'   # 指定模板

# 获取所有文章
def post_list(request,tag_slug=None):
    limit = 3                               # 每页显示的记录数
    object_list = Post.published.all()     # 获取所有帖子信息
    page = request.GET.get('page')  # get请求URL里面的page参数 http://abc.com/foobar?page=2 <a href="?page={{ page_number }}">
    tag = None
    if tag_slug:
        # 取出所有包含参数的标签
        tag = get_object_or_404(Tag,slug=tag_slug)
        # 过滤出包含标签的帖子
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list,limit)   # 实例化分页对象,把所有帖子按照每页3个记录显示
    try:
        posts = paginator.page(page)    # 获取某页对应的记录,如果获取到page=2 则取第二页信息
    except PageNotAnInteger:            # 如果页码不是整数
        posts = paginator.page(1)       # 取第一页记录
    except EmptyPage:                   # 如果页码太大,没有相应记录
        posts = paginator.page(paginator.num_pages)     # 则取最后一页
    return render(request,
                  'blog/post/list.html',
                  {'posts':posts,       # posts里包含所有帖子及分页后的帖子内容
                   'page':page,         # page里返回的是页面当前页数
                   'tag':tag})

def comment_reply(request,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    replys = comment.replys.filter(active=True)
    if request.method == 'POST':
        replys_form = ReplyForm(data=request.POST)
        if replys_form.is_valid():
            new_reply = replys_form.save(commit=False)
            new_reply.comment = comment
            new_reply.save()
    else:
        replys_form = ReplyForm()
    return render(request,'blog/post/comment_reply.html',
                  {'comment':comment,
                   'replys':replys,
                   'replys_form':replys_form})

# 获取某篇文章,参数年月日
def post_detail(request,year,month,day,post):
    # 查询出相应文章
    post = get_object_or_404(Post,slug=post,
                            status='published',
                             publish__year=year)
                             # publish__month=month,    # 查询为空,如何解决?
                             # publish__day=day)
    # 查过出所有状态为True(有效)的评论的集合
    comments = post.comments.filter(active=True)
    # replys = comments.replys.filter(active=True)
    if request.method == 'POST':
        # 表单实例
        comment_form = CommentForm(data=request.POST)
        # 验证表单数据是否有效
        if comment_form.is_valid():
            # 如果save() 时commit=False，那么它将返回一个还没有保存到数据库的对象
            # 没有保存之前可以任意修改这个model对象的值
            # save()方法创建的是modelForm对象,save()方法是给modelForm对象用的而不是表单实例
            new_comment = comment_form.save(commit=False)
            # 分配一个帖子给创建的评论对象
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    # 取回包含所有tags的list集合(QuerySet),返回的是元组,使用flat=True处理他得到列表
    post_tags_ids = post.tags.values_list('id',flat=True)
    # 取回所有包含这些tags的帖子,使用exclude过滤当前id的帖子
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    # 通过聚合函数Count生成一个统计字段same_tags,包含所有需要统计标签的总数,
    # 然后对其总数进行排序,并且当不同文章拥有相同标签时,我们只取前面四篇文章
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).\
                                            order_by('-same_tags','-publish')[:4]
    return render(request,
                  'blog/post/detail.html',
                  {'post':post,
                   'comments':comments,
                   'comment_form':comment_form,
                   'similar_posts':similar_posts})
                   # 'replys':replys})

# 邮件
def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')
    sent = False
    to = ""
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():                      # 使用is_valid方法验证提交数据是否有效
            cd = form.cleaned_data               # 将有效的数据转换为字典 {'name':'values'....}
            post_url = request.build_absolute_uri(  # 获取帖子完整的HTTP链接
                post.get_absolute_url()
            )
            # 主题
            subject = '{} ({}) recommends you reading "{}"'.\
                format(cd['name'],cd['email'],post.title)
            # 邮件内容
            message = 'Read "{}" at {} \n\n 发件人:{} \n 帖子内容:{}'.\
                format(post.title,post_url,cd['name'],cd['comments'])
            # 发送邮件(主题,内容,发件人,收件人)
            send_mail(subject,
                      message,
                      'shugaocheng@163.com',
                      [cd['to']])
            to = cd['to']
            sent = True
            # return HttpResponsePermanentRedirect('/blog/')
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,
                                                  'form':form,
                                                  'sent':sent,
                                                  'cd_to':to})

