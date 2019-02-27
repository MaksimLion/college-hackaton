from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserForm, ProfileForm, AuthForm
from django.contrib.auth import authenticate,login


def student(request):
    return render(request, 'student.html')


def sign_in(request):
    
    if request.method == 'POST':
        user_form = AuthForm(request.POST)
        
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return render(request, 'student.html')
                
            else:
                user_form = AuthForm()
                context = {
                    'user_form' : user_form,
                    'error' : 'неудачный вход, попробуйте ещё'
                }

                return render(request, 'sign-in.html', context)

        else:
            return redirect('/my_account')
    
    else:
        user_form = AuthForm()
        context = {
            'user_form' : user_form
        }
        return render(request, 'sign-in.html', context)


def sign_up(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_user.refresh_from_db()
            sex = profile_form.cleaned_data.get('sex')
            phone = profile_form.cleaned_data.get('phone')
            group = profile_form.cleaned_data.get('group')
            
            new_profile = Profile.objects.create(
                user=new_user, 
                sex=sex, 
                phone=phone, 
                group=group
            )

            new_profile.save()
            new_user.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return render(request, 'sign-up.html')

        return redirect('/')

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        context = {
            'profile_form' : profile_form,
            'user_form' : user_form
        }
        return render(request, 'sign-up.html', context)


def simple(request):
    return render(request, 'sign-up.html')
 

# def my_account(request):
#      if request.user.is_authenticated:
#          profile = request.user.get_profile()
#          profile.
         

