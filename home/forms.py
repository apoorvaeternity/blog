from django import forms
from .models import BlogEntries

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogEntries
        fields = '__all__'
        widgets = {
            "post": forms.Textarea(attrs={
                "style": "resize:none;",
                "cols": "10",
                "rows": "7"})}