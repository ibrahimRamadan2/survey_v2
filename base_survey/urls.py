from django.urls import path
from . import views

urlpatterns = [
    path("" , views.survey.as_view() )
]