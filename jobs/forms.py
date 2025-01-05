from django import forms
from django.contrib.auth.models import User
from .models import EmployerProfile, EmployeeProfile
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location', 'salary', 'employer']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_description', 'website']


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['resume']
