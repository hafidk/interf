from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)#per ficar asteriscs
        
        class Meta:
                model = User
                fields = ['username','email','password']

class LogForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)#asteriscs
        

class AnunciForm(forms.Form):
        titol = forms.CharField(max_length=30)
        descripcio = forms.CharField(max_length=300,widget=forms.Textarea)
        


