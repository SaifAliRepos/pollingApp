from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.site_header = 'Poller'
admin.site.site_title = 'Lets Poll'
admin.site.index_title = 'Welcome to Polling Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
  inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
