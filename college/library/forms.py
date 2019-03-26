from django import forms
from authentication.models import Subject


class NameModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%obj.name


class FilterForm(forms.Form):
    subject = NameModelChoiceField(
        label="Предмет",
        queryset = Subject.objects.all()
    )

    class Meta:
        fields = (
            'subject',
        )

