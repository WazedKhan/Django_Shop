from pyexpat import model
from django import forms
from users.models import User


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Enter Username", min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField( max_length=100, help_text='Required', error_messages={'required':'Sorry, You need an email'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'eamil', 'password1', 'password2')