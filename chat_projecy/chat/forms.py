from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, max_length=1000, required=True)
