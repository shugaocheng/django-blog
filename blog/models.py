from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager  # 标签应用
# import datetime
# Create your models here.

# 创建model manage,代替Post.objects
class PublishedManager(models.Manager):
    # 原get_queryset()
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


# # 用户
# class User(models.Model):
#     name = models.CharField()


# 帖子
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250,verbose_name='标题')
    # 设置unique_for_date,Django将不允许两个记录具有相同的slug和publish。
    # 这样就可以使用日期和帖子的slug来为所有帖子构建URL,因为他是唯一的
    slug = models.SlugField(max_length=250,unique_for_date='publish',verbose_name='标签')
    # 多对一关系(作者对帖子)
    # related_name指定User到Post的反向关系名 参考flask模型
    author = models.ForeignKey(User,related_name='blog_posts',verbose_name='作者')
    body = models.TextField(verbose_name='帖子内容')
    publish = models.DateTimeField(default=timezone.now,verbose_name='发布时间')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft',verbose_name='状态')

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()    # 实例化标签对象

    class Meta:
        ordering = ('-publish',)   # 发布时间倒序排序
        # db_table = 'Post'           # 指定数据库生成的表名

    def __str__(self):
        return 'Post by {} on {}'.format(self.title,self.publish)   # 返回Post模型对象的title

    # 获取帖子的绝对路径 例:2017/03/11/python.html,'blog:post_detail'证明是哪个视图
    # 在模板中使用
    def get_absolute_url(self):
        return reverse('blog:post_detail',  # ?????
                       args=[self.publish.year,
                             self.publish.strftime('%m'),   # strftime格式化字符串
                             self.publish.strftime('%d'),
                             self.slug])

class Comment(models.Model):
    """
    帖子评论
    """
    post = models.ForeignKey(Post,related_name='comments',verbose_name='帖子外键')  # 外键
    name = models.CharField(max_length=80,verbose_name='姓名')
    # authors = models.ForeignKey(User,related_name='comment_user',verbose_name='评论者')
    email = models.EmailField(verbose_name='邮箱')
    body = models.TextField(verbose_name='评论内容')
    created = models.DateTimeField(auto_now_add=True,verbose_name='发表时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    active = models.BooleanField(default=True,verbose_name='状态')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '该评论由{}发表在{}文章下,作者:{}'.format(self.name,self.post,self.post.author)

    def post_name(self):
        return u'%s' % self.post.publish

    def get_author(self):
        return '{}'.format(self.post.author)

class Reply(models.Model):
#     post = models.ForeignKey(Post)
    comment = models.ForeignKey(Comment,related_name='replys',verbose_name='评论')
    name = models.CharField(max_length=80)
    to_user = models.CharField(max_length=80)
    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    updated = models.DateTimeField(auto_now=True,verbose_name='修改时间')
    active = models.BooleanField(default=True,verbose_name='状态')
#     from_user = models.ForeignKey(User,related_name='reply_user',verbose_name='回复用户')
#     to_user = models.ForeignKey(User,verbose_name='被回复用户')
#     body = models.TextField(verbose_name='回复内容')
#     created = models.DateTimeField(auto_now_add=True,verbose_name='回复时间')
#     updated = models.DateTimeField(auto_now=True,verbose_name='修改时间')
#     active = models.BooleanField(default=True,verbose_name='状态')
#
    def __str__(self):
        return '该评论由{}回复{}'.format(self.name,self.to_user)
#
    class Meta:
        ordering = ('created',)