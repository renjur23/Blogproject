from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        
        
        labels={
            'b_title':"Block Title:",
            'a_name':"Author Name:",
            'b_image':"Blog_Image",
            'b_content':"Block Content",
            
             }
