#Jackson Lambert 6-6-19 Django Project
from django.shortcuts import render
from django.contrib.auth.models import User
from posts.models import Post
from django.views.generic import ListView
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

#THIS ENTIRE SECTION IS A MASSIVE WIP, I didn't have time to finish so it's not fully functional, but doesnt break the site
def get_user_profile(request, username,):
    #Get the username from the url
    user_name = User.objects.get(username=username)
    model = PageEditor
    #if forms are submitted, save data in instance variable
    if request.method == 'POST' :    
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            bio = instance.bio
            picture = instance.profilePicture
            instance.save()
            #Render those variables
            return render(request, 'profile.html', {"user_name":user_name, "form":form,
            "bio":bio, "picture":picture })
    else:
        form = ProfileEditForm()
   #just render the username and form if the form is yet to be submitted
    return render(request, 'profile.html', {"user_name":user_name, "form":form, })
    
    