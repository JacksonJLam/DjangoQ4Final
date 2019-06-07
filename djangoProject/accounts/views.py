from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignUp(generic.CreateView) :
    #Create a user creation form
    form_class = UserCreationForm
    #When a user is successfully created, go back to login screen
    success_url = reverse_lazy('login')
    #link to template
    template_name = 'signup.html'

