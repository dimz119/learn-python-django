from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect)
from django.urls import reverse
from django.template import loader
from polls.models import Question


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
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
