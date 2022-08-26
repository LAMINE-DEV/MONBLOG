from .models import Comment,Email,Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        



class CommentForm1(forms.ModelForm):
    #email = forms.EmailField(required=True,help_text='votre email')
    #subject = forms.CharField(required=True,help_text='sujet')
    #message=QuillField()
    #messagse = forms.CharField(widget=forms.Textarea, required=True,help_text='votre message')
    class Meta:
        model=Email
        fields=['email','subject','document','message']

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'