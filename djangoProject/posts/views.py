#Jackson Lambert 6-6-19 Django Project
from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 
from django.http import HttpResponse, HttpResponseRedirect
from .forms import * 
from .models import Post
from django.shortcuts import render
# User model POST and use template of post.html
class HomePageView(ListView):
    model = Post
    template_name = 'post.html'

def create(request):
    #if there is a post request, scrape the form, save form as instance
    #get the user in the current instance and save
    #or just render the page with the form
    if request.method == 'POST' :    
        #request both the text and files that are uploaded
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #If the form is valid, set the form data as an instance
            instance = form.save(commit=False)
            #request the user and save the user in a var
            instance.user = request.user
            instance.save()
            #redirect back a level in the page (redirects to home page)
            return HttpResponseRedirect('../')
    else:
        #Load form if it isn't loaded
        form = PostForm()
        return render(request,'upload.html',{'form':form})

#Get the title_id from the link, and then render the html with the title varaible saved
def post_specific(request, title_id):

    title = Post.objects.get(pk=title_id)
    return render(request, 'postSpecific.html', {'title': title})