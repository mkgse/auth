from . models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields=['first_name','last_name','username','email','address']
        labels = {'first_name':'First Name','last_name':'Last Name','profile_image':'Profile Picture','username':'User Name','email':'Email Id','address':'Address'}
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'address':forms.Textarea(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
     password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))