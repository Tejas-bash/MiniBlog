from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class Singup(UserCreationForm):
    password1 = forms.CharField(label='Passowrd',widget=forms.PasswordInput(attrs={'class':'form-control form_control'}))
    password2 = forms.CharField(label='Password Confirmation (again)',widget=forms.PasswordInput(attrs={'class':'form-control form_control'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        labels  = {'username':'Username','first_name':'Your First Name','last_name':'Your Last Name','email':'Your Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control form_control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control form_control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form_control'}),
            'email':forms.TextInput(attrs={'class':'form-control form_control'}),
        }

class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control form_control','autofocus':True}))
    password = forms.CharField(label=_('Password'),widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control form_control','autocomplete':'current-password'}),strip=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control form_control'}),
            'desc':forms.Textarea(attrs={'class':'form-control form_control'})
        }