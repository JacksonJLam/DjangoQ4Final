#Jackson Lambert 6-6-19 Django Project
from django.contrib import admin
from .models import PageEditor
# Register your models here.

#Registers the pageEditor model to admin page
admin.site.register(PageEditor)