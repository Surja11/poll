from django.contrib import admin
from .models import *
from django.utils import timezone
# Register your models here.

admin.site.site_header = "Poll Admin"
admin.site.site_title = "Poll Admin Area"
admin.site.index_title = "Welcome to Poll Admin area"

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3


class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields':['question']}), ('Date Information',{'fields':['published_date'],'classes':['collapse']}),]
  inlines = [ChoiceInline]
  list_display = ['question', 'published_date','is_approved']
  list_editable = ['is_approved']

class RequestedPollAdmin(admin.ModelAdmin):
  list_display = ['question', 'request_date', 'status']
  list_filter = ('status', 'request_date')
  search_fields = ('question',)
  actions = ['approve_requests']

  @admin.action(description="Approve selected pending poll requests")
  def approve_requests(self, request, queryset):
    for poll_request in queryset.filter(status = 'pending'):
      print("Approving request",poll_request.question)
      question = Question.objects.create(question = poll_request.question, is_approved = True,published_date = timezone.now() )
      print("Created question", question)
      Choice.objects.create(question = question, choice = poll_request.choice1)
      Choice.objects.create(question = question , choice = poll_request.choice2)
      Choice.objects.create(question = question, choice = poll_request.choice3)

      poll_request.status = 'approved'
      poll_request.save()
      self.message_user(request, f"Successfully approved poll requests.")




admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(RequestedPoll,RequestedPollAdmin)