from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import CourseView


app_name = 'courses_api'

urlpatterns = [
    path('', csrf_exempt(CourseView.as_view())),
    ]
