from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, Hoodform, BusinessForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Hood, Profile, Business, Post
from urllib import request
from django.db.models import Q


# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    # print(current_user)
    if request.method == 'POST':
        formhood = Hoodform(request.POST, request.FILES)
        if formhood.is_valid():
            upload = formhood.save(commit=False)
            upload.admin = request.user.profile
            # request.user.profile.save()
            upload.save()
            return redirect('home')
    else:

        formhood = Hoodform()
    welcome = "welcome to the home page"

    hoods = Hood.objects.all()
    return render(request, 'hood/home.html', {"welcome": welcome, "formhood": formhood, "hoods": hoods})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user

    if request.method == 'POST':
        formpro = ProfileForm(request.POST, request.FILES)
        if formpro.is_valid():
            upload = formpro.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('profile')
    else:

        formpro = ProfileForm()
    return render(request, 'hood/add_profile.html', {"formpro": formpro})


@login_required(login_url='/accounts/login/')
def profile(request):

    return render(request, 'hood/profile.html')


@login_required(login_url='/accounts/login/')
def neighborhood(request, hood_id):
    current_user = request.user

    # hood = get_object_or_404(Hood, pk=hood_id)
    if request.method == 'POST':
        formbiz = BusinessForm(request.POST, request.FILES)
        if formbiz.is_valid():
            addbiz = formbiz.save(commit=False)
            addbiz.hood = hood_id
            # upload.admin = current_user
            # request.user.profile.save()
            addbiz.save()
            return redirect('hood')
    else:

        formbiz = BusinessForm()

    if request.method == 'POST':
        formpost = PostForm(request.POST, request.FILES)
        if formpost.is_valid():
            addpost = formpost.save(commit=False)
            addpost.hoodwatch = hood_id
            addpost.user = current_user
            addpost.save()
            return redirect('hood')
    else:

        formpost = PostForm()

        # post = get_object_or_404(Post, hoodwatch=hood_id)
        hood = get_object_or_404(Hood, pk=hood_id)
        # business = get_object_or_404(Business, hood=hood_id)
    return render(request, 'hood/hood.html', {"formbiz": formbiz, "formpost": formpost, "hood": hood})


@login_required(login_url='/accounts/login/')
def search(request):

    query = request.GET.get('q')
    print(query)
    if query:
        results = Hood.objects.filter(
            Q(name__icontains=query))
    else:
        results = Hood.objects.all()
    return render(request, 'pages/search.html', {'results': results})
