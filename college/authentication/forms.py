from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'sex',
            'group',
            'phone',
        )


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )