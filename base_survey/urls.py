from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Surveys.as_view() ) , 
    path("<int:id>" , views.SurveyDetails.as_view())
     
]