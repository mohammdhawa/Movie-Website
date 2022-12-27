from django.shortcuts import render, redirect
from .models import Profile
from .forms import SignForm, UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user) 
            return redirect('/accounts/profile-edit')
    else: # show form
        form = SignForm()
    
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user = request.user)
    
    context = {'profile': profile}
    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myform = profileform.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    
    context = {'userform': userform, 'profileform': profileform}
    return render(request, 'profile/profile_edit.html', context)
