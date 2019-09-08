from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from . models import  Profile,Image,Rating
from django.contrib.auth.models import User
from .forms import NewProfileForm,NewPostForm,Rate
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    profile = Profile.objects.all()
    ratings = Rating.objects.all()
    return render(request,'index.html',{"images":images,"profile":profile ,"ratings":ratings})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.save()
        return redirect('welcome')

    else:
        form = NewPostForm()
    return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')      
def new_profile(request,id):
    user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form":form,"user":user})
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    posts=Image.objects.filter(profile_id=current_user.id)
    ratings = Rating.objects.filter(profile_id=current_user_id)
    return render(request, 'profile-page.html',{"profile":profile,"posts":posts,"ratings":ratings})
def ratings(request,id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = Rate(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile=current_user
            post.save()
        return redirect('welcome')

    else:
        form = Rate()
    return render(request, 'ratings.html', {"form": form})
