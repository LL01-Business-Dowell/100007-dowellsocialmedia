import requests
# Create your views here.
from django.shortcuts import render

from gform2website import settings
from website.forms import UserEmailForm, IndustryForm, SentencesForm
from website.models import Sentences, SentenceResults, SelectedResult


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
            object = sentencesForm.cleaned_data['object'].lower()
            subject = sentencesForm.cleaned_data['subject']
            verb = sentencesForm.cleaned_data['verb']
            objdet = sentencesForm.cleaned_data['object_determinant']
            objnum = sentencesForm.cleaned_data['object_number']
            subjdet = sentencesForm.cleaned_data['subject_determinant']
            subjnum = sentencesForm.cleaned_data['subject_number']
            adjective = sentencesForm.cleaned_data['adjective']

            # this code below is commented because the team lead requested that the code generates different sentences
            # # now for the grammar part of the sentence
            # tense = sentencesForm.cleaned_data['tense']
            # progressive = sentencesForm.cleaned_data['progressive']
            #
            # perfect = sentencesForm.cleaned_data['perfect']
            #
            # negated = sentencesForm.cleaned_data['negated']
            #
            # passive = sentencesForm.cleaned_data['passive']
            #
            # sentence_art = sentencesForm.cleaned_data['sentence_art']
            # modal_verb = sentencesForm.cleaned_data['modal_verb']
            # # save to database
            # sentence = Sentences(user=user,
            #                      object=object,
            #                      subject=subject,
            #                      verb=verb,
            #                      adjective=adjective,
            #                      object_determinant=objdet,
            #                      subject_determinant=subjdet,
            #                      object_number=objnum,
            #                      subject_number=subjnum,
            #                      tense=tense,
            #                      progressive=progressive,
            #                      passive=passive,
            #                      perfect=perfect,
            #                      negated=negated,
            #                      sentence_art=sentence_art,
            #                      modal_verb=modal_verb
            #
            #                      )
            # if progressive:
            #     progressive = 'progressive'
            # if perfect:
            #     perfect = 'perfect'
            # if negated:
            #     negated = 'negated'
            # if passive:
            #     passive = 'passive'
            # # create an api query string
            # querystring = {
            #     "object": object,
            #     "subject": subject,
            #     "verb": verb,
            #     "objmod": adjective,
            #     'subjdet': subjdet,
            #     'objdet': objdet,
            #     'objnum': objnum,
            #     'passive': passive,
            #     'progressive': progressive,
            #     'modal': modal_verb,
            #     'perfect': perfect,
            #     'subjnum': subjnum,
            #     'sentencetype': sentence_art,
            #     'negated': negated,
            #     'tense': tense
            #
            # }
            # headers = {
            #     'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
            #     'x-rapidapi-key': settings.LINGUA_KEY
            # }
            #
            # response = requests.request("GET", url, headers=headers, params=querystring)
            #
            # # sentence.sentence = response.json()['sentence']
            # # sentence.save()
            # return render(request, 'answer_display.html', {'sentence': response.json()['sentence']})
            def api_call(grammar_arguments=None):
                if grammar_arguments is None:
                    grammar_arguments = {}
                querystring = {
                    "object": object,
                    "subject": subject,
                    "verb": verb,
                    "objmod": adjective,
                    'subjdet': subjdet,
                    'objdet': objdet,
                    'objnum': objnum,
                    'subjnum': subjnum,

                }
                type_of_sentence = ' '
                iter_sentence_type = []
                if 'tense' in grammar_arguments:
                    querystring['tense'] = grammar_arguments['tense'].capitalize()
                    iter_sentence_type.append(grammar_arguments['tense'].capitalize())
                if 'progressive' in grammar_arguments:
                    querystring['progressive'] = 'progressive'
                    iter_sentence_type.append(grammar_arguments['progressive'])

                if 'perfect' in grammar_arguments:
                    querystring['perfect'] = 'perfect'
                    iter_sentence_type.append(grammar_arguments['perfect'])

                if 'negated' in grammar_arguments:
                    querystring['negated'] = 'negated'
                    iter_sentence_type.append(grammar_arguments['negated'])

                if 'passive' in grammar_arguments:
                    querystring['passive'] = 'passive'
                    iter_sentence_type.append(grammar_arguments['passive'])

                if 'modal_verb' in grammar_arguments:
                    querystring['modal'] = grammar_arguments['modal_verb']

                if 'sentence_art' in grammar_arguments:
                    querystring['sentencetype'] = grammar_arguments['sentence_art']
                type_of_sentence = type_of_sentence.join(iter_sentence_type)

                headers = {
                    'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
                    'x-rapidapi-key': settings.LINGUA_KEY
                }

                return [requests.request("GET", url, headers=headers, params=querystring).json()['sentence'],
                        type_of_sentence]

            sentence_grammar = Sentences.objects.create(user=user,
                                                        object=object,
                                                        subject=subject,
                                                        verb=verb,
                                                        adjective=adjective,
                                                        object_determinant=objdet,
                                                        subject_determinant=subjdet,
                                                        object_number=objnum,
                                                        subject_number=subjnum
                                                        )

            tenses = ['past', 'present', 'future']
            # modal_verbs = [
            #     '-none-', 'can', 'may',
            #     'must', 'ought', 'shall',
            #     'should', 'would'
            # ]

            # sentence_arts = [
            #     'Declarative',
            #     'Yes-no',
            #     'What(object)',
            #     'Who(subject)', ]
            other_grammar = ['passive', 'progressive', 'perfect', 'negated']
            results = []
            count = 0
            for tense in tenses:
                for grammar in other_grammar:
                    sentence_results = SentenceResults(sentence_grammar=sentence_grammar)
                    arguments = {tense: tense, grammar: grammar}
                    api_result = api_call(arguments)
                    sentence_results.sentence = api_result[0]
                    sentence_results.sentence_type = api_result[1]
                    sentence_results.save()
                    results.append(sentence_results)

            sentences_dictionary = {
                'sentences': results,
                # 'result_id': sentence_grammar.pk
            }
            print(sentences_dictionary)
            return render(request, 'answer_display.html', context=sentences_dictionary)
    return render(request, 'stepwise.html', context=forms)


def selected_result(request):
    if request.method == 'POST':
        # result_id = request.POST.get('result_id')
        selected_result = request.POST.get('gridRadios')
        sentence_result = SentenceResults.objects.get(pk=selected_result)
        selected_result_obj = SelectedResult.objects.create(
            sentence_result= sentence_result,
            selected_sentence=sentence_result.sentence)
        return render(request, 'display_selected_result.html', {'sentence': selected_result_obj})
