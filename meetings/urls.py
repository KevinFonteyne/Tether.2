from django.urls import path
from .views import Calendar

urlpatterns = [
    path('meetings/', Calendar.as_view(), name='meetings'),
]