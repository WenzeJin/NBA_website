from django.forms import ModelForm
from .models import DatePicker
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DatePickerForm(ModelForm):

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = DatePicker
        fields = ['date']


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
