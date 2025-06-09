from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
  question = models.CharField(max_length = 200)
  is_approved = models.BooleanField(default = False)
  published_date = models.DateTimeField('date published')
  voted_user = models.ManyToManyField(User)

  def  __str__(self):
    return self.question

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice = models.CharField(max_length = 200)
  votes = models.IntegerField(default = 0)

  def __str__(self):
    return self.choice

class RequestedPoll(models.Model):

  STATUS_CHOICES = [
    ('pending' , 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
  ]

  question  = models.CharField(max_length = 200)
  choice1 = models.CharField(max_length=200)
  choice2 = models.CharField(max_length = 200)
  choice3 = models.CharField(max_length = 200)
  request_date = models.DateTimeField(auto_now_add = True)
  status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = 'pending')
  admin_notes = models.TextField(blank = True)

  def __str__(self):
    return f"{self.question} (Status : {self.status})"