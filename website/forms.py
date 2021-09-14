from django import forms

from website.models import User, IndustryData, Sentences


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class IndustryForm(forms.ModelForm):
    class Meta:
        model = IndustryData
        fields = ('target_industry', 'target_product')
        widgets = {
            'target_industry': forms.Select(attrs={'class': 'form-select'}),
            'target_product': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SentencesForm(forms.ModelForm):
    class Meta:
        model = Sentences
        fields = ('subject_adjective','subject','object_adjective', 'object', 'verb', 'adjective')
        widgets = {
            'subject_adjective': forms.Select(attrs={'class': 'form-select col-6'}),
            'subject': forms.Select(attrs={'class': 'form-select col-6'}),
            'object_adjective': forms.Select(attrs={'class': 'form-select col-6'}),
            'object': forms.TextInput(attrs={'class': 'form-control col-6'}),
            'verb': forms.TextInput(attrs={'class': 'form-control'}),
            'adjective': forms.TextInput(attrs={'class': 'form-control'}),
        }
