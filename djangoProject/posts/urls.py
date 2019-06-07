#Jackson Lambert 6-6-19 Django Project
from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf import settings
from .views import HomePageView, create
from django.conf.urls.static import static
from . import models
from . import views
urlpatterns = [
    #Home page of the post app, holds all the posts
    re_path(r'^$', HomePageView.as_view(), name='post'),
    #The upload form page
    path('upload/', create, name='add_post'),
    #Gives a number link to each post, the int value is the id # of the title
    path('<int:title_id>/', views.post_specific, name='post_specific'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)