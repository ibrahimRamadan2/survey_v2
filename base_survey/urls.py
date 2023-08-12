from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Survey.as_view() ) , 
    path("<int:id>" , views.SurveyDetails.as_view())
     
]