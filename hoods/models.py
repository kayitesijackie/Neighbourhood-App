from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from pyuploadcare.dj.models import ImageField
import datetime
from tinymce.models import HTMLField


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Hood(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='hood', null= True)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE,related_name='hoods', null=True)
    description = models.TextField(default='Random group', null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    datecreated = models.DateField(auto_now_add=True, null=True)
    occupants_count = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(default="Your Name")
    prof_pic = models.ImageField(upload_to='profile', null=True)
    bio = models.TextField(default="Tell us something")
    hoodwatch = models.ForeignKey(Hood, on_delete=models.CASCADE,blank=True, null=True, related_name='people')
    email = models.EmailField(max_length=75, null=True)

    def __str__(self):
        return f'Profile {self.user}'

    @classmethod
    def get_profile(cls, name):
        profile = Profile.objects.filter(name=name)
        return profile


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except Exception as error:
            print(error)


class Business(models.Model):
    name = models.TextField()
    b_owner = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=75, null=True)
    description = models.TextField(default='hood business')
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE,null=True,related_name='business')


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    Text = models.TextField(null=True)
    hoodwatch = models.ForeignKey(Hood, on_delete=models.CASCADE,null=True, related_name='posts')
