from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
	#this will store the most recent 5 questions
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	#formats the question for display
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
#Gives the question id
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
#gives the results of the poll
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
#gives what question you are voting on
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)