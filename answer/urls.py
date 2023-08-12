from django.urls import path, include
from . import views

urlpatterns=[
    path("" , views.AnswerView.as_view()),
    path("statistics/<int:survey_id>" , views.AnswerDetailsView.as_view())
]