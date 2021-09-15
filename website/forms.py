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
    TENSES = (
        ('Present', 'Present'),
        ('Past', 'Past'),
        ('Future', 'Future'),

    )
    NUMBERS = (
        ('Singular', 'Singular'),
        ('Plural', 'Plural'),

    )
    # convert tenses to radio button input through the form class
    tense = forms.ChoiceField(choices=TENSES, widget=forms.RadioSelect())
    # create radio buttons for singular/plural of subject and object
    subject_number = forms.ChoiceField(choices=NUMBERS, widget=forms.RadioSelect())
    object_number = forms.ChoiceField(choices=NUMBERS, widget=forms.RadioSelect())

    class Meta:
        model = Sentences
        fields = (
            'subject_determinant', 'subject', 'subject_number', 'object_determinant', 'object', 'object_number',
            'verb', 'adjective', 'tense', 'sentence_art',
            'modal_verb', 'progressive', 'perfect', 'passive', 'negated')
        widgets = {
            'subject_determinant': forms.Select(attrs={'class': 'form-select'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'object_determinant': forms.Select(attrs={'class': 'form-select'}),
            'object': forms.TextInput(attrs={'class': 'form-control'}),
            'verb': forms.TextInput(attrs={'class': 'form-control'}),
            'adjective': forms.TextInput(attrs={'class': 'form-control'}),
            # for part two of the form
            'tense': forms.Select(attrs={'class': 'form-select'}),
            'sentence_art': forms.Select(attrs={'class': 'form-select'}),
            'modal_verb': forms.Select(attrs={'class': 'form-select'}),

        }
