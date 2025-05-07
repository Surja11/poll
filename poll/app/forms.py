from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
class RegisterForm(UserCreationForm):
  email = forms.EmailField(required = True)
  class Meta:
    model = User
    fields =['username', 'email', 'password1','password2']

class LoginForm(AuthenticationForm):
  username = forms.CharField(label = 'Email or Username')
  

class PollForm(forms.Form):
  question= forms.CharField()
  choice1= forms.CharField()
  choice2 = forms.CharField()
  choice3 = forms.CharField()