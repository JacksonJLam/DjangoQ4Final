#Jackson Lambert 6-6-19 Django Project
from django import forms
from .models import *

class PostForm(forms.ModelForm):
#Set name of the upload form fields
    class Meta:
        model = Post
        fields = ['title', 'cover', 'description', ]