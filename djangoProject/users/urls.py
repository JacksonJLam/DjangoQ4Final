#Jackson Lambert 6-6-19 Django Project
from . import views
from django.urls import path, include, re_path
from django.conf.urls import url, include
#Url pattern fo profiles is profiles/<username> then call the user profile function
urlpatterns = [
    url(r'(?P<username>[\w.@+-]+)/$', views.get_user_profile, name='profilepage'),
]