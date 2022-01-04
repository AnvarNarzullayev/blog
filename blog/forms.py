from django import forms
from .models import Blog, Comment


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','slug','description','img','category_id','tag',]
    




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']