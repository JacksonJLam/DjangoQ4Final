#Jackson Lambert 6-6-19 Django Project
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

#Define the fields and str name of itself
class PageEditor(models.Model):
    bio = models.TextField()
    profilePicture = models.ImageField(upload_to='media/images/')
    
    
    def __str__(self):
        return self.bio