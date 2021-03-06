from django import forms
from .models import Issue, Comments


class IssueForm(forms.ModelForm):
    """Issue form, uses type to differentiate between bugs and issues"""
    class Meta:
        model = Issue
        fields = ('title', 'description', 'type')


class CommentForm(forms.ModelForm):
    """Allows Users to comment on a specific issue"""
    class Meta:
        model = Comments
        fields = ['comments']
