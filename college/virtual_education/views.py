from django.shortcuts import render, redirect
from django.http import FileResponse
from django.views.generic.edit import CreateView
from django.views import View
from authentication.models import Profile
from .forms import FilterLab, CreateReportForm
from .models import Report, Lab


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class MyAccountView(View):
    template_name = 'student.html'
    form_class = CreateReportForm
    
    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.pk)
        form = self.form_class()
        context = {
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
            'phone' : profile.phone,
            'sex' : profile.sex,
            'group' : profile.group,
            'career' : profile.career.all(),
            'skills' : profile.skills.all(),
            'mark' : profile.mark,
            'favourite_subjects' : profile.favorite_subject.all(),
            'achievements' : profile.achievements.all(),
            'photo' : profile.photo,
            'form' : form
        }
        return render(request, self.template_name, context)


class LabsView(View):
    form_class = FilterLab
    template_name = 'labs.html'

    def get(self, request, *args, **kwargs):
        labs = Lab.objects.all().prefetch_related('subject')
        form = self.form_class()
        context = {
            'labs' : labs,
            'forms' : form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            labs = Lab.objects.filter(subject=subject.pk)
            form = self.form_class()
            context = {
                'labs' : labs,
                'forms' : form
            }
        return render(request, self.template_name, context)


class LabStatistics(View):
    template_name = 'statistics.html'

    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.pk)
        context = {
            'reports': Report.objects.filter(user=profile.pk).prefetch_related('subject')
        }
        return render(request, self.template_name, context)


class CreateReport(View):
    form_class = CreateReportForm

    def post(self, request):
        title = request.POST['title']
        form = CreateReportForm(request.POST, request.FILES)

        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            report = form.cleaned_data.get('file')

        author = Profile.objects.get(user_id=request.user.pk)
        group = author.group
        name = request.user.get_full_name()
        Report.objects.create(
            name_executor=name,
            group=group,
            file=report,
            title=title,
            user=author,
            subject=subject
        )
        return redirect('/my_account')
    

class LabDetail(View):
    
    def get(self, requetst, lab_id):
        lab = Lab.objects.get(pk=lab_id)
        return FileResponse(lab.read_file.open(mode='rb'), content_type='application/pdf')
