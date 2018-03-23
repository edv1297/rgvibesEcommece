from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                "placeholder":"First name",
                                "display":"none"}))

    last_name = forms.CharField(label="",max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                 "placeholder":"Last name"}))
    email = forms.EmailField(label="",max_length=35,
            widget=forms.EmailInput(
                    attrs = {"class":"form-control",
                             "placeholder":"Email address"}))
    subject = forms.CharField(label="",max_length=40,
            widget = forms.TextInput(
                    attrs = {"class":"form-control",
                             "placeholder":"Subject"}))

    Message = forms.CharField(label="",
                widget = forms.Textarea(
                    attrs = {"class":"form-control",
                            "placeholder":"Talk to us"}))

class LoginForm(forms.Form):
    user_name = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Username",
                                "display":"none"}))

    password = forms.CharField(label="", max_length=25,
                widget = forms.PasswordInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Password",
                                "display":"none"}))

class RegisterForm(forms.Form):
    email = forms.EmailField(label="",max_length=35,
            widget=forms.EmailInput(
                    attrs = {"class":"form-control",
                            "placeholder":"Email address"}))

    user_name = forms.CharField(label="", max_length=25,
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
                                "placeholder":"Password",
                                "display":"none"}))
    country = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control",
                                "placeholder":"Where are you from?",
                                "display":"none"}))
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_verification')

        if password2 != password:
            raise forms.ValidationError("Passwords must match :(")
        return data
