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



class AnunciForm(forms.ModelForm):
        titol = forms.CharField(max_length=30)
        descripcio = forms.CharField(max_length=300)
        




