from django import forms
from .models import Comment,Reply

# Form表单-->邮箱
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25,label='姓名',error_messages={'required':'请输入您的称呼',
                                                                    'max_length':'称呼太长'})
    email = forms.EmailField(label='发件人邮箱',error_messages={'required':'请输入您的邮箱地址',
                                                              'invalid':'格式不正确'})
    to = forms.EmailField(label='收件人邮箱',error_messages={'required':'请输入收件人的邮箱',
                                                           'invalid':'格式不正确'})
    comments = forms.CharField(required=False,widget=forms.Textarea,label='内容')

# ModelForm表单-->评论
# 因为models里已经有评论模型,所以不需要再去重新建立一个表单
class CommentForm(forms.ModelForm):
    class Meta:
        # 声明使用Comment来构建表单,Django会解析model并动态的创建表单
        model = Comment
        # 明确指明评论表单需要用到的列
        fields = ('name','email','body')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name','to_user','body')