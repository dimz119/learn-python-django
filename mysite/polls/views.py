from django.http import (
    HttpResponse,
    HttpResponseRedirect)
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.forms import SurveyForm
from django.template import loader
from polls.models import(
    Choice,
    Survey,
    Question
)


# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     # return HttpResponseRedirect(
#     #     reverse('detail', args=[1]))
#     # return HttpResponseRedirect(
#     #     reverse('detail', kwargs={'question_id': 1}))
#     ctx = {
#         "greetings": "Hello there!",
#         "location": {
#             "city": "Seoul",
#             "country": "South Korea"
#         },
#         "languages": ["Korean", "English"]
#     }
#     return render(request, 'polls/main.html', context=ctx)

# # using template
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

# using render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def survey(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SurveyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            # # update
            # survey = Survey.objects.get(pk=1)
            # form = SurveyForm(request.POST, instance=survey)

            form.save()

            # print(form.cleaned_data['user_name'])
            # print(form.cleaned_data['user_age'])

            return HttpResponseRedirect(reverse('polls:thanks'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SurveyForm()

    # return render(request, 'polls/survey.html', {'form': form})
    return render(request, 'polls/survey_custom.html', {'form': form})

def thanks(request):
    return render(request, 'polls/thanks.html', {})