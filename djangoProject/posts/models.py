#Jackson Lambert 6-6-19 Django Project
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

#Fields and data that will have data scraped from it
class Post(models.Model):
    #post title field
    title = models.TextField()
    #Post image field
    cover = models.ImageField(upload_to='media/images/')
    #Post description field
    description = models.TextField(null=True, blank=True)
    #Yoinks the user that is uploading
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #Save the time it was published
    dateTime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
