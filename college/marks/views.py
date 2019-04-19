from django.shortcuts import render
from django.views import View
from authentication.models import Profile 
from .models import Mark

class MarkView(View):
    
    template_name = ''

    def get(self, request):
        profile = Profile.objects.get(user_id=request.user.pk)
        marks = Mark.objects.filter(user=profile.id)
        context = {
            'marks' : marks
        }
        return render(request, self.template_name, context)
        
