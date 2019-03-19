from django import forms
from .models import Report

class CreateReportForm(forms.Form):
    title = forms.Charfield()
    file = forms.FileField()
    
    class Meta:
        model = Report
        fields = (
            'title',
            'file',
        )