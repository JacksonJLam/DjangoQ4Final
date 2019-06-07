#Jackson Lambert 6-6-19 Django Project
from django import forms
from .models import *
#Form for data POSTing
class ProfileEditForm(forms.ModelForm):

    class Meta:
        #Set the model ot PageEditor from models.py
        model = PageEditor
        #Name the fields
        fields = ['bio', 'profilePicture', ]