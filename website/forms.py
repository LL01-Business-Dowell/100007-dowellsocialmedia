from django import forms

from website.models import User, IndustryData, Sentences


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'


class IndustryForm(forms.ModelForm):
    class Meta:
        model = IndustryData
        fields=('target_industry','target_product')



class SentencesForm(forms.ModelForm):
    class Meta:
        model = Sentences
        fields=('subject','object','verb','adjective')

