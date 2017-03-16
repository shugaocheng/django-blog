from django.contrib import admin
from .models import Post,Comment,Reply
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # 列表顶部显示的字段名称
    list_display = ['title','slug','author','publish','status']
    # 列表右侧过滤器
    list_filter = ('status','created','publish','author')
    # 列表页搜索框
    search_fields = ('title','body')
    #
    prepopulated_fields = {'slug':('title',)}
    # 编辑表单界面的主键
    raw_id_fields = ('author',)
    # 时间
    date_hierarchy = 'publish'
    # 根据状态和时间排序
    ordering = ['status','publish']
    # filter_horizontal = ('author',)

class CommentAdmin(admin.ModelAdmin):
    list_display =['name','email','post','created','active','get_authors']
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')
    raw_id_fields = ('post',)

    # 获取作者字段
    def get_authors(self,obj):
        return obj.post.author
    # 设置该字段的显示名称
    get_authors.short_description = '作者'

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment','name','to_user','body','created','active']
    list_filter = ('active','created','updated')
    search_fields = ('body','comment')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply,ReplyAdmin)