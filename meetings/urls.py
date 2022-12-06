from django.urls import path
from .views import CalendarView
from . import views

app_name = ''
urlpatterns = [
    path('', CalendarView.as_view(), name='calendar'),
]