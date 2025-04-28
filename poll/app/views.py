from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404
# Create your views here.

#Get questions and display them
def index(request):
  latest_questions = Question.objects.order_by('-published_date')[:5];

  context = {'latest_questions': latest_questions}

  return render(request, 'app/index.html',context)

# Show specific questions and choices
def detail(request, question_id):
  try:
    question = Question.objects.filter(pk = question_id)
  except Question.DoesNotExist:
    raise Http404("Question doesnot exists")
  return render(request, 'app/result.html',{'question':question})


def results(request,question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, 'app/result.html',{'question': question})
