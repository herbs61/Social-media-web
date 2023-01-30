from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    # Creating a registration form
class UserRegistrationForm(forms.ModelForm):
    
    # You want to create you own label so that it does not automatically give you password1 and password2 
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    
    # This gives you the fields that will be in the registration form of the user
    class Meta:
        model = User
        fields={'username','email','first_name'}
        
        # This one checks of the two passwords match
        def check_password(self):
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError('Password do not match')
            return self.cleaned_data['password2']
    