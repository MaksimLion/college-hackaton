from django import forms
from .models import Report

class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = (
            'title',
            'file',
        )