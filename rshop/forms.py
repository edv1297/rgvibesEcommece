from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    first_name = forms.CharField(label="", max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control mb-2",
                                "placeholder":"First name",
                                "display":"none"}))

    last_name = forms.CharField(label="",max_length=25,
                widget = forms.TextInput(
                        attrs = {"class":"form-control mb-2",
                                 "placeholder":"Last name"}))
    email = forms.EmailField(label="",max_length=35,
            widget=forms.EmailInput(
                    attrs = {"class":"form-control mb-2",
                             "placeholder":"Email address"}))
    subject = forms.CharField(label="",max_length=40,
            widget = forms.TextInput(
                    attrs = {"class":"form-control mb-2",
                             "placeholder":"Subject"}))

    Message = forms.CharField(label="",
                widget = forms.Textarea(
                    attrs = {"class":"form-control mb-2",
                            "placeholder":"Talk to us"}))
