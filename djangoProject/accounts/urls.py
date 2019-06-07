#Accounts URL page

from django.urls import path

from . import views
#Url pattern to take users to the signup page
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]