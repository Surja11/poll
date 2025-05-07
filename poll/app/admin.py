from django.contrib import admin
from .models import *
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






admin.site.register(Question,QuestionAdmin)
