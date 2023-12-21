from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from captcha import ReCaptchaField
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField()


# create or register a user(model form)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']    

#authenticate a user (model form)


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=TextInput())

    captcha= ReCaptchaField(widget=ReCaptchaV2Checkbox())
        