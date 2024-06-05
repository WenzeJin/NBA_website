"""forms.py: BBS表单
This file is used to define the forms of BBS app.
By using django forms, we can easily deploy the form in the front-end.

author: Wenze Jin
date: 2024-05-15
"""

from django.contrib.auth.models import User
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['nickname', 'email', 'birthday', 'slogan']
        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
            'slogan': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(
            attrs={'class': 'ckeditor', 'name': 'content'}),
        label='',
        required=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'abstract', 'content']
        widget = {
            'content': RichTextUploadingField(verbose_name='content'),
        }


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['rate', 'content']
        widget = {
            'rate': forms.NumberInput(attrs={'class': 'form-control-range'}),
        }

