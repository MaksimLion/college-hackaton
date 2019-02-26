from django.forms import ModelForm
from .models import Profile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields =  '__all__'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'sex',
            'group',
        )