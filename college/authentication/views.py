from django.shortcuts import render, redirect
from django.views import View
from django.http import FileResponse
from .models import Profile
from virtual_education.models import Report, Lab
from .forms import UserForm, ProfileForm, AuthForm
from virtual_education.forms import CreateReportForm, FilterLab
from django.contrib.auth import authenticate,login


class SignUpView(View):

    user_form_class = UserForm
    profile_form_class = ProfileForm
    template_name = 'sign-up.html'

    def get(self, request):
        user_form = self.user_form_class()
        profile_form = self.profile_form_class()
        context = {
            'profile_form' : profile_form,
            'user_form' : user_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = self.user_form_class(request.POST)
        profile_form = self.profile_form_class(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            new_user.refresh_from_db()
            sex = profile_form.cleaned_data.get('sex')
            phone = profile_form.cleaned_data.get('phone')
            group = profile_form.cleaned_data.get('group')

            new_profile = Profile.objects.create(
                user = new_user,
                sex = sex,
                phone = phone, 
                group = group
            
            )

            return redirect('auth/sign_in/')     


class SignInView(View):

    form_class = AuthForm
    template_name = 'sign-in.html'

    def get(self, request):
        user_form = self.form_class()
        context = {
            'user_form' : user_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = self.form_class(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(
                request,
                username = username,
                password = password
            )

            login(request, user)
            return redirect('/my_account')


def logout_view(request):
    logout(request)
    return redirect('sign_in/')

         

