from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Company, Job, Application
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "website", "is_active"]
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["company", "title", "location", "salary_min", "salary_max", "status"]
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["job", "status", "applied_date", "notes"]
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]