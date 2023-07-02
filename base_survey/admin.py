from django.contrib import admin
from .models import BaseSurvey
from .models import Question
from .models import QuestionType
# Register your models here.


class BaseSurveyAdmin(admin.ModelAdmin):
    fields = ['name' , 'end_at']

admin.site.register(BaseSurvey, BaseSurveyAdmin)