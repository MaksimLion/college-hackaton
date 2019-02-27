from django.shortcuts import render
from .models import Profile
from .forms import UserForm, ProfileForm

def signin(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid:
            new_user = user_form.save()


    else:
        user_form = UserForm()
        context = {
            'user_form' : user_form
        }
        return render(request, 'signin.html', context)

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid and profile_form.is_valid:
            new_user = user_form.save()
            new_profile = Profile.objects.create(user=new_user)
            new_profile.save()


    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        context = {
            'profile_form' : profile_form,
            'user_form' : user_form
        }
        return render(request, 'signup.html', context)


def simple(request):
    return render(request, 'signup.html')
