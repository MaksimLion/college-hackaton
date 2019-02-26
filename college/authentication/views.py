from django.shortcuts import render
#

# def auth(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = ProfileForm(request.POST)
        
#         if user_form.is_valid and profile_form.is_valid:
#             new_user = user_form.save()
#             new_profile = Profile.objects.create(user=new_user)
#             new_profile.save()


#     else
#         user_form = UserForm()
#         profile_form = ProfileForm()
#         context = {
#             'profile_form' : profile_form,
#             'user_form' : user_form
#         }
#         return()


def simple(request):
    return render(request, 'base.html')
