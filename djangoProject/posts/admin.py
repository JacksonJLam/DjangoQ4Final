#Jackson Lambert 6-6-19 Django Project
from django.contrib import admin

from .models import Post
# Register your models here.
#Register the posts model into admin
class PostAdmin(admin.ModelAdmin):
    field = ['pub_date']
admin.site.register(Post, PostAdmin)