from django import forms

from website.models import User, IndustryData, Sentences


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User


class IndustryForm(forms.ModelForm):
    class Meta:
        model = IndustryData


class SentencesForm(forms.ModelForm):
    class Meta:
        model = Sentences
