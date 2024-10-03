from django.urls import path
from . import views

urlpatterns = [
    path('process-question/', views.process_question, name='process_question'),
]