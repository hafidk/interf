from django import forms
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)#per ficar asteriscs
        
        class Meta:
                model = User
                fields = ['username','email','password']

class LogForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)#per ficar asteriscs
        
        class Meta:
                model = User
                fields = ['username','password']



class RegForm(forms.Form):
        nom = forms.CharField(max_length=30)
        email = forms.EmailField()
        pwd = forms.CharField(max_length=30)

