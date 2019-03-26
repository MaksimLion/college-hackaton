from django.shortcuts import render
from django.views import View
from .models import BenefitLink, Book
from .forms import FilterForm

class BenefitLinksView(View):
    template_name = ''
    form_class = FilterForm

    def get(self, request):
        form = self.form_class()
        links = BenefitLink.objects.all()
        context = {
            'form' : form,
            'links' : links 
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            labs = BenefitLink.objects.filter(subject=subject.pk)
            form = self.form_class()
            context = {
                'links' : labs,
                'form' : form
            }
        return render(request, self.template_name, context)


class Book(View):
    template_name = ''
    form_class = FilterForm

    def get(self, request):
        form = self.form_class()
        books = Book.objects.all()
        context = {
            'form' : form,
            'books' : books 
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            books = Book.objects.filter(subject=subject.pk)
            form = self.form_class()
            context = {
                'books' : books,
                'form' : form
            }
        return render(request, self.template_name, context)
