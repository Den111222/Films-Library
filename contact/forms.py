from django import forms

"""Нужно в файле fields заменить стандартный 'from django.utils.translation import ugettext_lazy as _' на 
'from django.utils.translation import gettext_lazy as _' и тогда все заработает"""
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """Форма пописки по email"""
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