from django.shortcuts import render, redirect
from .models import Profile
from virtual_education.models import Report, Lab
from .forms import UserForm, ProfileForm, AuthForm
from virtual_education.forms import CreateReportForm, FilterLab
from django.contrib.auth import authenticate,login


def student(request):
    return render(request, 'student.html')


def sign_in(request):
    
    if request.method == 'POST':
        user_form = AuthForm(request.POST)
        
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password')
            user = authenticate(
                request,
                username=user_form.cleaned_data.get('username'), 
                password=user_form.cleaned_data.get('password'),
            )

            #if user is not None and user.is_active:
            login(request, user)
            
            return redirect('/my_account')
                
            # else:
            #     user_form = AuthForm()
            #     context = {
            #         'user_form' : user_form,
            #         'error' : 'неудачный вход, попробуйте ещё'
            #     }

            #     return render(request, 'sign-in.html', context)

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
            # new_user = authenticate(request, username=username, password=password)
            #login(request, new_user)
            return redirect('/sign_in/')

        return redirect('/')

    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        context = {
            'profile_form' : profile_form,
            'user_form' : user_form
        }
        return render(request, 'sign-up.html', context)
 

def my_account(request):

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        profile = Profile.objects.get(user_id=request.user.pk)
        phone = profile.phone
        photo = profile.photo
        sex = profile.sex
        group = profile.group
        mark = profile.mark
        career = profile.career.all()
        skills = profile.skills.all()
        achievements = profile.achievements.all()
        favorite_subjects = profile.favorite_subject.all()
        form = CreateReportForm()
        context = {
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'phone' : phone,
            'sex' : sex,
            'group' : group,
            'career' : career,
            'skills' : skills,
            'mark' : mark,
            'favorite_subjects' : favorite_subjects,
            'achievements' : achievements,
            'photo' : photo,
            'form' : form,
        }

        return render(request, 'student.html', context)
    else:
        return redirect('/sign_in/')


def send_report(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.POST['file']
        subject_form = CreateReportForm(request.POST)
        if subject_form.is_valid():
            subject_object = subject_form.cleaned_data['subject']
        author = Profile.objects.get(user_id=request.user.pk)
        group = author.group
        name = request.user.get_full_name()
        Report.objects.create(name_executor=name, group=group, file=file, title=title, user=author, subject=subject_object)
        return redirect('/my_account/')
 

def statistics(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.pk)
        report_statuses = Report.objects.filter(user=profile.pk).prefetch_related('subject')
        context = {
            'reports' : report_statuses
        }
        return render(request, 'statistics.html', context)


def labs(request):
    if request.method == 'GET':
        labs = Lab.objects.all().prefetch_related('subject')
        filter_form = FilterLab()
        context = {
            'labs' : labs,
            'forms' : filter_form,
        }

        return render(request, 'labs.html', context)

    elif request.method == 'POST':
        subject_form = FilterLab(request.POST)
        if subject_form.is_valid():
            subject = subject_form.cleaned_data.get('subject')
            labs = Lab.objects.filter(subject=subject.pk)
            filter_form = FilterLab()
            context = {
            'labs' : labs,
            'forms' : filter_form,
            }
        return render (request, 'labs.html', context)




def lab_detail(request,lab_id):
    lab = Lab.objects.get(pk=lab_id)
    with open(lab.read_file, 'rb') as pdf:
        text = pdf.readline()
    context = {
        'text' : text
    }
    return render(request, 'lab_detail.html', context)


def logout_view(request):
    logout(request)
    return redirect('sign_in/')

         

