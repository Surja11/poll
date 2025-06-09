from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.http import Http404, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages, auth
# Create your views here.

#Get questions and display them
def register(request):
  if request.method == "POST":
    register_form = RegisterForm(request.POST  or None)
    # print(register_form.errors)
    if register_form.is_valid():
      # print("Form is valid")
      user= register_form.save()
      user.save()
      login(request, user)
      return redirect('/')
      
  else:
    register_form = RegisterForm()
  context = {'register_form': register_form}
  return render(request, 'app/register.html',context)

def loginuser(request):
  if request.method == "POST":
      
      login_form = LoginForm(request, data = request.POST)
      # print(login_form.errors)
      if login_form.is_valid():
        
        user = login_form.get_user()
        login(request, user)
        return redirect('/')
  else:
      login_form = LoginForm()
  context = {'login_form': login_form}
  return render(request, 'app/login.html', context)

def logout(request):
  auth.logout(request)
  return redirect('/')

def index(request):
  latest_questions = Question.objects.order_by('-published_date')[:5];

  context = {'latest_questions': latest_questions}

  return render(request, 'app/index.html',context)

# Show specific questions and choices
@login_required
def detail(request, question_id):
  try:
    question = Question.objects.get(pk = question_id)
  except Question.DoesNotExist:
    raise Http404("Question doesnot exists")
  return render(request, 'app/detail.html',{'question':question})


def results(request,question_id):
  question = get_object_or_404(Question, pk = question_id)
  return render(request, 'app/result.html',{'question': question})

@login_required
def vote(request, question_id):
  #print(request.POST['choice'])
  question = get_object_or_404(Question, pk = question_id)
  user = request.user
  try:
    selected_choice = question.choice_set.get(pk = request.POST['choice'])
  except:
    return render(request, 'app/detail.html',{'question': question,  'error_message':  "You didn't select a choice",})
  
  else:
    if user in question.voted_user.all():
      messages.error(request,"You have already voted")
      return redirect('/')
    else:
      question.voted_user.add(user)
      selected_choice.votes += 1
      selected_choice.save()
      return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

@login_required
def pollquestion(request):
  if request.method == "POST":
    poll_form = PollForm(request.POST)
    if poll_form.is_valid():
      RequestedPoll.objects.create(
        question = request.POST.get('question'),
        choice1 = request.POST.get('choice1'),
        choice2 = request.POST.get('choice2'),
        choice3 = request.POST.get('choice3'),

      )
      messages.success(request, 'Your poll request has been submitted for approval')
      return redirect('/')

  poll_form = PollForm()
  context = {'poll_form': poll_form}
  return render(request, 'app/pollqn.html', context)



def resultsData(request, question_id):
  votedata = []
  question = Question.objects.get(id = question_id)
  votes = question.choice_set.all()
  
  for i in votes:
    votedata.append({i.choice: i.votes})

  return JsonResponse(votedata, safe = False)