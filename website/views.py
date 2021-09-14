import requests
# Create your views here.
from django.shortcuts import render

from gform2website import settings
from website.forms import UserEmailForm, IndustryForm, SentencesForm
from website.models import Sentences


def index(request):
    emailForm = UserEmailForm()
    industryForm = IndustryForm()
    sentencesForm = SentencesForm()
    forms = {'emailForm': emailForm, 'industryForm': industryForm, 'sentencesForm': sentencesForm}
    if request.method == "POST":
        emailForm = UserEmailForm(request.POST)
        industryForm = IndustryForm(request.POST)
        sentencesForm = SentencesForm(request.POST)
        if emailForm.is_valid() and industryForm.is_valid() and sentencesForm.is_valid():
            url = "https://linguatools-sentence-generating.p.rapidapi.com/realise"
            user = emailForm.save()
            industry = industryForm.save(commit=False)
            industry.user = user
            industry.save()
            object = sentencesForm.cleaned_data['object']
            subject = sentencesForm.cleaned_data['subject']
            verb = sentencesForm.cleaned_data['verb']
            objdet = sentencesForm.cleaned_data['object_adjective']
            subjdet = sentencesForm.cleaned_data['subject_adjective']
            adjective = sentencesForm.cleaned_data['adjective']
            sentence = Sentences(user=user, object=object, subject=subject, verb=verb, adjective=adjective)
            querystring = {"object": object, "subject": subject, "verb": verb, "objmod": adjective, 'subjdet': subjdet,
                           'objdet': objdet}
            headers = {
                'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
                'x-rapidapi-key': settings.LINGUA_KEY
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            sentence.sentence = response.json()['sentence']
            sentence.save()
            return render(request, 'answer_display.html', {'sentence': response.json()['sentence']})
    return render(request, 'stepwise.html', context=forms)
