from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
    email = forms.EmailField(label="",max_length=35,
            widget=forms.EmailInput(
                    attrs = {"class":"form-control",
                            "placeholder":"Email address"}))


class LoginForm(forms.Form):
    user_name = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control mb-2",
                                "placeholder":"Username",
                                "display":"none"}))

    password = forms.CharField(label="", max_length=25,
                widget = forms.PasswordInput(
                        attrs = {"class":"form-control mb-2",
                                "placeholder":"Password",
                                "display":"none"}))

class RegisterForm(forms.Form):
    email = forms.EmailField(label="",max_length=35,
            widget=forms.EmailInput(
                    attrs = {"class":"form-control",
                            "placeholder":"Email address"}))

    username = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Username",
                                "display":"none"}))

    password = forms.CharField(label="", max_length=25,
                widget = forms.PasswordInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Password",
                                "display":"none"}))

    password_verification = forms.CharField(label="", max_length=25,
                widget = forms.PasswordInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Verify password",
                                "display":"none"}))
    country = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                "placeholder":"What country are you from?",
                                "display":"none"}))


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already being used.")
        return username

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_verification')

        if password2 != password:
            raise forms.ValidationError("Passwords must match :(")
        return data
