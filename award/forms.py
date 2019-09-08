from .models import Profile,Image,Rating
from django import forms
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['']        
class Rate(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ['']
