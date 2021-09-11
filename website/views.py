import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from formtools.wizard.views import SessionWizardView

from gform2website import settings
from website.forms import UserEmailForm, IndustryForm, SentencesForm
from website.models import User, IndustryData, Sentences
import requests


class FormWizard(SessionWizardView):
    form_list = [UserEmailForm, IndustryForm, SentencesForm]
    template_name = 'done.html'

    def done(self, form_list, **kwargs):
        print('done')

        # url = "https://linguatools-sentence-generating.p.rapidapi.com/realise"
        #
        # form_data = [form.cleaned_data for form in form_list]
        # email = form_data[0]['email']
        # user = User.objects.create(email=email)
        # target_industry = form_data[1]['target_industry']
        # target_product = form_data[1]['target_product']
        # industry = IndustryData.objects.create(user=user, target_industry=target_industry,
        #                                        target_product=target_product)
        #
        # object = form_data[2]['object']
        # subject = form_data[2]['subject']
        # verb = form_data[2]['verb']
        # adjective = form_data[2]['adjective']
        # sentence = Sentences(user=user, object=object, subject=subject, verb=verb, adjective=adjective)
        # querystring = {"object": object, "subject": subject, "verb": verb, 'adjective': adjective}
        # print("{} is the query string".format(querystring))
        # headers = {
        #     'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
        #     'x-rapidapi-key': settings.LINGUA_KEY
        # }
        #
        # response = requests.request("GET", url, headers=headers, params=querystring)
        # # sentence.sentence = response.text
        # # sentence.save()
        # return HttpResponse('<p>'+response.text+'</p>')


def index(request):
    return render(request, 'home.html')
