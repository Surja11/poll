from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import *
# Create your views here.

#Get questions and display them
def register(request):
  register_form = RegisterForm()
  context = {'register_form': register_form}
  return render(request, 'app/register.html',context)

def login(request):
  login_form = LoginForm()
  context = {'login_form': login_form}
  return render(request, 'app/login.html', context)

def index(request):
  latest_questions = Question.objects.order_by('-published_date')[:5];

  context = {'latest_questions': latest_questions}

  return render(request, 'app/index.html',context)

# Show specific questions and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk = question_id)
  except Question.DoesNotExist:
    raise Http404("Question doesnot exists")
  return render(request, 'app/detail.html',{'question':question})


def results(request,question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, 'app/result.html',{'question': question})

def vote(request, question_id):
  #print(request.POST['choice'])
  question = get_object_or_404(Question, pk = question_id)
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except:
    return render(request, 'app/detail.html',{'question': question,  'error_message':  "You didn't select a choice",})
  
  else: 
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))