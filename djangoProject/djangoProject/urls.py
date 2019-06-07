"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from . import views
#djangoProject URLs
urlpatterns = [
    #admin page path
    path('admin/', admin.site.urls),
    #Creating User
    path('accounts/', include('accounts.urls')),
    #login stuff
    path('accounts/', include('django.contrib.auth.urls')),
    #index page path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #Post subapp main path
    path('post/', include('posts.urls'), name='post'),
    #main path to the profile
    path('profile/', include('users.urls'), name='profile')
    ]
#if in debug mode, django will server media from this url
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
 
