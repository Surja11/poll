from django import forms

class RegisterForm(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  email = forms.EmailField()
  password = forms.CharField(widget = forms.PasswordInput)
  password2 = forms.CharField(widget = forms.PasswordInput)

class LoginForm(forms.Form):
  email = forms.EmailField()
  password = forms.CharField(widget = forms.PasswordInput)
  

class PollForm(forms.Form):
  question= forms.CharField()
  choice1= forms.CharField()
  choice2 = forms.CharField()
  choice3 = forms.CharField()