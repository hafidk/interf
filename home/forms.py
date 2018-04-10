from django import forms


class RegForm(forms.Form):
        nom = forms.CharField(max_length=30)
        email = forms.EmailField()
        pwd = forms.CharField(max_length=30)

class LogForm(forms.Form):
        nom=forms.CharField(max_length=30)
        pwd = forms.CharField(max_length=30)
