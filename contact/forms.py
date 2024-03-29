from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """Форма подписки по email"""
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = ("email", "captcha",)
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent", "placeholder": "yor email..."})
        }
        labels = {
            "email": "",
        }