from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from .models import *
from .views import home, profile, neighborhood, add_profile, search

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^profile$', profile, name='profile'),
    url(r'^hood/(?P<id>\d+)/$', neighborhood, name='hood'),
    url(r'^add_profile', add_profile, name='add_profile'),
    url(r'^search', search, name='search')


]
