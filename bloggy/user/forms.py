from django import forms
from django.forms.widgets import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField(label='Username/Email')
    password = forms.CharField(widget=PasswordInput, label='Password')

    def get_username(self):
        username = cleaned_data['userame']
        return username

    def get_password(self):
        password = cleaned_data['password']
        return password
