from django import forms
from .models import Profile, Hood, Business, Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email"]


class Hoodform(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ["name","location"]


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ["name", "b_owner", "contact", "email", "description"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["Text"]
