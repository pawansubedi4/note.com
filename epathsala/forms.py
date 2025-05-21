from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,unit,exam

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class UnitsForm(forms.ModelForm):
    class Meta:
        model = unit
        fields = ['class1', 'sub', 'pub','major','unit_num','unit_pdf',]

class ExamForm(forms.ModelForm):
    class Meta:
        model = exam
        fields = ['ter', 'class1', 'sub','major','pdf','scl']

