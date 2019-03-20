from django import forms
from authentication.models import Subject
from .models import Report


class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.name


class CreateReportForm(forms.Form):
    subject = NameModelChoiceField(
        label = 'Предмет',
        queryset = Subject.objects.all(),
    )
    file = forms.FileField()
    
    class Meta:
        fields = (
           'subject',
           'file',
        )


class FilterLab(forms.Form):
    subject = NameModelChoiceField(
        label="Предмет",
        queryset = Subject.objects.all()
    )

    class Meta:
        fields = (
            'subject',
        )
